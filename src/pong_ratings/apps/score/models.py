from django.contrib.auth.models import User
from django.db import models

class Score(models.Model):
    user = models.ForeignKey(User)
    score = models.IntegerField()

    def __unicode__(self):
        return '%s - %s' % (self.user, self.score)

    def calculate_game(self, score):
        self.handicap_self = 10
        self.handicap_other = -10


