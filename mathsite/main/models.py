from django.db import models


class RankingTo10(models.Model):
    PlayerName = models.CharField(max_length=24)
    Score = models.IntegerField()

    def __str__(self):
        return self.PlayerName

class RankingTo50(models.Model):
    PlayerName = models.CharField(max_length=24)
    Score = models.IntegerField()

    def __str__(self):
        return self.PlayerName