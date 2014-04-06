from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.views.generic import View
import account.views
from models import Rating
from forms import Game


class SignupView(account.views.SignupView):

    def after_signup(self, form):
        rating = Rating(user=self.created_user,
                       score=500)
        rating.save()
        super(SignupView, self).after_signup(form)


class HandicapView(View):
    def get(self, request):
        scores = Rating.objects.all()
        try:
            curr_users_score = Rating.objects.get(user = request.user)
        except ObjectDoesNotExist:
            rating = Rating(user=request.user,
                           score=500)
            rating.save()
            curr_users_score = rating

        [score.calculate_game(curr_users_score) for score in scores]

        return render_to_response(
            'handicap.html', {
                'curr_users_score': curr_users_score,
                'scores': scores},
            context_instance=RequestContext(request))

class RecordView(View):
    def get(self, request, score_id):
        score = Rating.objects.get(pk=score_id)
        form = Game()
        return render_to_response(
            'record.html', {
                'form': form,
                'score': score,
            },
            context_instance=RequestContext(request))

    def post(self, request, score_id):
        curr_users_score = Rating.objects.get(user = request.user)
        other_users_score = Rating.objects.get(pk=score_id)
        form = Game(request.POST)
        if form.is_valid():
            self_score = int(form.cleaned_data.get('self_score'))
            other_score = int(form.cleaned_data.get('other_score'))
            if self_score > other_score:
                curr_users_score.score += self_score
                other_users_score.score -= other_score
            else:
                curr_users_score.score -= self_score
                other_users_score.score += other_score
            curr_users_score.save()
            other_users_score.save()

        return redirect('handicap')
