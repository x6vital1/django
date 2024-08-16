import datetime

from django.test import TestCase, Client
from parcel import models as parcel_models
from post_machine import models as post_machine_models
from django.contrib.auth.models import User


# Create your tests here.
class TestParcel(TestCase):
    fixtures = ['data']

    def setUp(self):
        test_pmachine = post_machine_models.PostMachine.objects.get(pk=1)
        test_locker = post_machine_models.Locker.objects.filter(post_machine=test_pmachine)[0]
        self.test_parcel = parcel_models.Parcel()
        self.test_parcel.recipient = User.objects.create_user(username='test_user', password='test_password')
        self.test_parcel.sender = 'test sender'
        self.test_parcel.size = 10
        self.test_parcel.post_machine_recipient = test_pmachine
        self.test_parcel.locker = test_locker
        self.test_parcel.order_datetime = datetime.datetime.now(datetime.UTC)
        self.test_parcel.open_datetime = datetime.datetime.now(datetime.UTC)
        self.test_parcel.status = False
        self.test_parcel.save()
        self.test_parcel.locker.status = True
        self.test_parcel.locker.save()

    def test_parcel(self):
        actual_locker = post_machine_models.Locker.objects.get(pk=self.test_parcel.locker.pk)
        self.assertEqual(actual_locker.status, True)
        c = Client()
        c.login(username='test_user', password='test_password')
        response = c.post(f'/parcels/get_parcel/{self.test_parcel.pk}/')
        self.assertEqual(response.status_code, 302)
        actual_parcel = parcel_models.Parcel.objects.get(pk=self.test_parcel.pk)
        self.assertEqual(actual_parcel.status, True)
        actual_locker = post_machine_models.Locker.objects.get(pk=self.test_parcel.locker.pk)
        self.assertEqual(actual_locker.status, True)
        print(f'Parcel delivering test passed')
