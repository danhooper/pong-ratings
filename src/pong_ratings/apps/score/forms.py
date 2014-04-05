from django import forms
from django.contrib.auth.models import User


class Game(forms.Form):
    self_score = forms.IntegerField(label='My score')
    other_score = forms.IntegerField(label='Their score')
