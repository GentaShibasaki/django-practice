from distutils.log import Log
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

from ..models import Diary

class LoggedInTestCase(TestCase):
  # Unique test case class by overriding common preparation procedure for each test class

  def setUp(self):
    # password for test user
    self.password = 'password'

    # generate instance method for test user and
    # hold it in instance variable
    self.test_user = get_user_model().objects.create_user(username='test_user', email="test@example.com", password=self.password)

    # log into by test user
    self.client.login(email=self.test_user.email, password=self.password)

class TestDiaryCreateView(LoggedInTestCase):
  # test class for DiaryCreateView

  def test_create_diary_success(self):
    # confirm diary creation feature

    # post parameter
    params = {
      'title': 'test',
      'content': 'test content',
      'photo1': '',
      'photo2': '',
      'photo3': '',
    }

    # Post - execute new diary creation 
    response = self.client.post(reverse_lazy('diary:diary_create'), params)

    # confirm to refirect to diary list page
    self.assertRedirects(response, reverse_lazy('diary:diary_list'))

    # confirm that diary data is registered on DB
    self.assertEqual(Diary.objects.filter(title='test').count(), 1)

  def test_create_diary_failure(self):
    # confirm a fail of creating new diary data

    # Post - execute new diary creation 
    response = self.client.post(reverse_lazy('diary:diary_create'))

    # Cause an error by not filling a required field
    self.assertFormError(response, 'form', 'title', 'このフィールドは必須です。')

class TestDiaryUpdateView(LoggedInTestCase):
  
  def test_update_diary_success(self):

    diary = Diary.objects.create(user=self.test_user, title='before editing')

    params = {'title': 'after editing'}

    response = self.client.post(reverse_lazy('diary:diary_update', kwargs={'pk':diary.pk}), params)

    self.assertRedirects(response, reverse_lazy('diary:diary_detail', kwargs={'pk':diary.pk}))

    self.assertEqual(Diary.objects.get(pk=diary.pk).title, 'after editing')


  def test_update_diary_failure(self):

    response = self.client.post(reverse_lazy('diary:diary_update', kwargs={'pk':999}))

    self.assertEqual(response.status_code, 404)

class TestDiaryDeleteView(LoggedInTestCase):

  def test_delete_diary_success(self):
    diary = Diary.objects.create(user=self.test_user, title='Delete diary')

    response = self.client.post(reverse_lazy('diary:diary_delete', kwargs={'pk':diary.pk}))

    self.assertRedirects(response, reverse_lazy('diary:diary_list'))

    self.assertEqual(Diary.objects.filter(pk=diary.pk).count(), 0)

  def test_delete_diary_failure(self):

    response = self.client.post(reverse_lazy('diary:diary_delete', kwargs={'pk':999}))

    self.assertEqual(response.status_code, 404)
    