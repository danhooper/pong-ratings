from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.template import RequestContext
from django.views.generic import View
from models import Score
from forms import Game


class HandicapView(View):
    def get(self, request):
        scores = Score.objects.all()
        curr_users_score = Score.objects.get(user = request.user)
        [score.calculate_game(curr_users_score) for score in scores]

        return render_to_response(
            'handicap.html', {
                'curr_users_score': curr_users_score,
                'scores': scores},
            context_instance=RequestContext(request))

class RecordView(View):
    def get(self, request, score_id):
        score = Score.objects.get(pk=score_id)
        form = Game()
        return render_to_response(
            'record.html', {
                'form': form,
                'score': score,
            },
            context_instance=RequestContext(request))

    def post(self, request, score_id):
        curr_users_score = Score.objects.get(user = request.user)
        other_users_score = Score.objects.get(pk=score_id)
        form = Game(request.POST)
        if form.is_valid():
            curr_users_score.score -= int(form.cleaned_data.get('self_score'))
            curr_users_score.save()
            other_users_score.score -= int(form.cleaned_data.get('other_score'))
            other_users_score.save()

        return redirect('handicap')
