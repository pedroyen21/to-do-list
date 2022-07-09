from django.test import TestCase, Client
from django.urls import reverse
from tasks.models import Task
from users.models import User

class TasksTestCase(TestCase):
   
   def setUp(self) -> None:
      self.client = Client()
      self.testuser = User.objects.create(username='testuser', password='123')
      self.testtask = Task.objects.create(user=self.testuser ,name='testtask1', description='testing', conc_date='2022-07-03')  

   def test_create_tasks(self) -> None:
      response = self.client.post(reverse('tasks:create_task'), {
         'name':'testtask1',
         'description': 'test description', 
         'conc_date': '2022-07-03'
      })
      self.assertEqual(response.status_code, 302)
      self.assertEqual(Task.objects.first().name, 'testtask1')
     
   def test_edit_task_get(self) -> None:
      response = self.client.get(reverse('tasks:edit_task', args=[Task.objects.first().id]))   
      self.assertEqual(response.status_code, 200)

   def test_edit_task_post(self) -> None:
      task = Task.objects.first()
      response = self.client.post(
         reverse('tasks:edit_task', kwargs={'pk': task.id}), 
         {
         'name' : 'new test name',
         'description' : 'new test description', 
         'conc_date' : '2024-09-03'
         }
      )      
      task.refresh_from_db()

      self.assertEqual(response.status_code, 302)
      self.assertEqual(task.name, 'new test name')
      self.assertEqual(task.description, 'new test description')
      self.assertEqual(str(task.conc_date), '2024-09-03')
     
   
