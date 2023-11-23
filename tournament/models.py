from django.db import models
from django.db.models import Min, Max

class Team(models.Model):
    country = models.CharField(max_length=3, unique=True)

    @classmethod
    def matches_played(self):
        return TeamMatch.objects.filter(team=self).count()

    @classmethod
    def matches_won(self):
        return TeamMatch.objects.filter(team=self).aggregate(Max('batting_score'))
    
    @classmethod
    def matches_lost(self):
        return TeamMatch.objects.filter(team=self).aggregate(Min('batting_score'))

class Match(models.Model):
    date = models.DateField()


class TeamMatch(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE,
                             related_name='team_matches')
    match = models.ForeignKey(Match, on_delete=models.CASCADE,
                              related_name='team_matches')
    batting_score = models.IntegerField()
    batting_wickets = models.IntegerField()
    batting_overs = models.IntegerField()
