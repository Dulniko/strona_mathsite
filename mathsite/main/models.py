from django.db import models
from django.contrib.auth.models import User

class RankingTo10(models.Model):
    PlayerName = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Score = models.IntegerField()

    def __str__(self):
        return self.PlayerName.username if self.PlayerName else "Anonim"


class RankingTo50(models.Model):
    PlayerName = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Score = models.IntegerField()

    def __str__(self):
        return self.PlayerName.username if self.PlayerName else "Anonim"
