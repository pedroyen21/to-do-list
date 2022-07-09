from django.test import TestCase
from users.models import User

# Create your tests here.

class TestUsers(TestCase):
   def setUp(self) -> None:
      user1 = User.objects.create(username='testuser1', password='12345')
      user2 = User.objects.create(username='testuser2', password='12345')

   def test_user(self) -> None:
      self.assertEqual(str(User.objects.get(username='testuser1')), 'testuser1')
      self.assertEqual(str(User.objects.get(username='testuser2')), 'testuser2')