from django.test import TestCase
from election.models import Candidate, User
from django.urls import reverse

# Create your tests here.


class CandidateDetailsViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(username='test', password='pass1234')
        Candidate.objects.create(user=user, name='test', roll='1234')

    def test_view_url_exists_at_desired_location(self):
        candidate = Candidate.objects.get(id=1)
        print(candidate.post)
    #     resp = self.client.get('/election/candidate/', {'pk': candidate.id})
    #     self.assertEqual(resp.status_code, 200)

    # def test_view_url_accessible_by_name(self):
    #     resp = self.client.get(reverse('candidate_details', kwargs={'pk': 1}))
    #     self.assertEqual(resp.status_code, 200)


class CandidateProfileViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_candidates = 10
        for candidate_num in range(number_of_candidates):
            user = User.objects.create(username='test %s' % candidate_num, password='pass1234')
            Candidate.objects.create(user=user, name='Candidate %s' % candidate_num, roll='roll%s' % candidate_num)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/election/candidate_profiles')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('candidate_profiles'))
        self.assertEqual(resp.status_code, 200)


class VotePreviewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_candidates = 10
        for candidate_num in range(number_of_candidates):
            user = User.objects.create(username='test %s' % candidate_num, password='pass1234')
            Candidate.objects.create(user=user, name='Candidate %s' % candidate_num, roll='roll%s' % candidate_num)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/election/voter/vote_preview')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('vote_preview'))
        self.assertEqual(resp.status_code, 200)


# class VoteConfirmViewTest(TestCase):
#
#     @classmethod
#     def setUpTestData(cls):
#         user = User.objects.create(username='test1', password='pass1234')
#         Candidate.objects.create(user=user, name='test', roll='1234')
#
#     def test_view_url_exists_at_desired_location(self):
#         candidate = Candidate.objects.get(id=1)
#         print(candidate.post)
#         resp = self.client.get('/election/voter/vote_confirm', {'pk': candidate.id})
#         self.assertEqual(resp.status_code, 200)

    # def test_view_url_accessible_by_name(self):
    #     resp = self.client.get(reverse('candidate_details', kwargs={'pk': 1}))
    #     self.assertEqual(resp.status_code, 200)



