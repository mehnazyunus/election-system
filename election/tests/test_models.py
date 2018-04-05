from django.test import TestCase

from election.models import Voter, Election, User


class VoterModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='test', password='pass1234')
        Voter.objects.create(user=user, name='test', roll='1234')


    def test_name_label(self):
        voter = Voter.objects.get(id=1)
        field_label = voter._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_data(self):
        voter = Voter.objects.get(id=1)
        self.assertEquals(voter.name, 'test')
        self.assertEquals(voter.user.username, 'test')
        self.assertEquals(voter.roll, '1234')
