from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from post_machine.models import PostMachine, Locker


# Create your models here.

class Parcel(models.Model):
    recipient = models.ForeignKey(User, on_delete=models.CASCADE)
    sender = models.CharField(max_length=100)
    size = models.IntegerField()
    post_machine_recipient = models.ForeignKey(PostMachine, on_delete=models.CASCADE)
    locker = models.ForeignKey(Locker, null=True, blank=True, default=None, on_delete=models.DO_NOTHING)
    order_datetime = models.DateTimeField('order datetime', blank=True, null=True)
    open_datetime = models.DateTimeField('open datetime', blank=True, null=True)
    update_datetime = models.DateTimeField('update datetime', default=datetime.now)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.recipient} {self.sender} {self.size}'

@receiver(post_save, sender=Parcel)
def update_status_on_parcel_put_to_locker(sender, instance, created, **kwargs):
    if instance.status is False:
        if instance.locker is not None:
            parcel_locker = Locker.objects.get(pk=instance.locker.pk)
            parcel_locker.status = False
            parcel_locker.save()
