from django.test import TestCase
from myapp.models import User, Group
# Create your tests here.
class UserTestCase(TestCase):
    def testQuery(self):
        user = User()
        # self.assertEqual(, '')

class GroupTestCase(TestCase):
    def testQuery(self):
        group = Group()
