from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class PostMachine(models.Model):
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

class Locker(models.Model):
    size = models.IntegerField()
    post_machine = models.ForeignKey(PostMachine, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)