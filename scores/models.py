from django.db import models
from candidates.models import Candidates
from account.models import CustomUser 
# Create your models here.



class Scores(models.Model):
    user_id = models.OneToOneField(CustomUser, related_name="user_id", on_delete=models.CASCADE)
    candidates_id = models.OneToOneField(Candidates, related_name="candidates_id", on_delete=models.CASCADE)
    general = models.CharField(max_length=250)
    knowledge = models.CharField(max_length=250)
    manifesto = models.CharField(max_length=250)
    globals = models.CharField(max_length=250)
    value = models.CharField(max_length=250)
    total = models.CharField(max_length=250)
    