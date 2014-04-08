from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.views.generic import View
import account.views
from models import Rating
from forms import GameFormSet




class SignupView(account.views.SignupView):

    def after_signup(self, form):
        rating = Rating(user=self.created_user,
                       score=500)
        rating.save()
        super(SignupView, self).after_signup(form)


class HandicapView(View):
    def get(self, request, recorded=False):
        scores = Rating.objects.all()
        try:
            curr_users_score = Rating.objects.get(user = request.user)
        except ObjectDoesNotExist:
            rating = Rating(user=request.user,
                           score=500)
            rating.save()
            curr_users_score = rating

        [score.calculate_game(curr_users_score) for score in scores]
        message = None
        if recorded:
            message = 'Score Recorded'
        return render_to_response(
            'handicap.html', {
                'curr_users_score': curr_users_score,
                'scores': scores,
                'message': message},
            context_instance=RequestContext(request))

class RecordView(View):
    def get(self, request, score_id, formset = None):
        score = Rating.objects.get(pk=score_id)
        if not formset:
            formset = GameFormSet()
        return render_to_response(
            'record.html', {
                'formset': formset,
                'score': score,
            },
            context_instance=RequestContext(request))

    def calculate_score(self):
        score_diff = self.winner_score - self.loser_score
        change = ((self.loser.score / 100) * score_diff +
                  (1000 - self.winner.score)/100)
        self.winner.score += change
        if self.winner.score > 1000:
            self.winner.score = 1000
        self.loser.score -= change
        if self.loser.score < 100:
            self.loser.score = 100

    def post(self, request, score_id):
        curr_users_score = Rating.objects.get(user = request.user)
        other_users_score = Rating.objects.get(pk=score_id)
        formset = GameFormSet(request.POST)
        if formset.is_valid():
            for form in formset.cleaned_data:
                try:
                    self_score = int(form.get('self_score'))
                    other_score = int(form.get('other_score'))
                except TypeError:
                    # the form must not have been filled in
                    continue
                if self_score > other_score:
                    self.winner = curr_users_score
                    self.loser = other_users_score
                    self.winner_score = self_score
                    self.loser_score = other_score
                else:
                    self.loser = curr_users_score
                    self.winner = other_users_score
                    self.winner_score = other_score
                    self.loser_score = self_score
                self.calculate_score()
                curr_users_score.save()
                other_users_score.save()
        else:
            return self.get(request, score_id, formset)
        return redirect('handicap_rec', recorded='recorded')
