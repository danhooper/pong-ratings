from django.contrib.auth.models import User
from django.db import models

class Rating(models.Model):
    user = models.ForeignKey(User)
    score = models.IntegerField()

    def __unicode__(self):
        return '%s - %s' % (self.user, self.score)

    def calculate_game(self, score):
        handicap = int(abs(self.score - score.score)/50)
        if self.score < score.score:
            if handicap <= 10:
                self.handicap_self = handicap
                self.handicap_other = 0
            else:
                self.handicap_other = 10
                self.handicap_self = 10 - handicap
        else:
            if handicap <= 10:
                self.handicap_other = handicap
                self.handicap_self = 0
            else:
                self.handicap_other = 10
                self.handicap_self = 10 - handicap
