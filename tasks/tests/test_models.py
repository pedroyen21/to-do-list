from django.test import TestCase
from tasks.models import Task
from users.models import User

class TasksTestCase(TestCase):
   
   def setUp(self) -> None:
      user1 = User.objects.create(username='testuser1', password='12345')
      user2 = User.objects.create(username='testuser2', password='12345')

      task1 = Task.objects.create(user=user1, name='testtask1', description='testing', conc_date='2022-07-03')
      task2 = Task.objects.create(user=user2, name='testtask2', description='testing', conc_date='2022-07-03')
         
   
   def test_right_users_for_tasks(self) -> None:
      task1_user = Task.objects.get(name='testtask1').user
      self.assertEqual(str(task1_user), 'testuser1')
      
      task2_user = Task.objects.get(name='testtask2').user
      self.assertEqual(str(task2_user), 'testuser2')