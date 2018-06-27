from django.test import TestCase
from .models import User, Group
# Create your tests here.
class UserTestCase(TestCase):
    def testQuery(self):
        user = User()
        #Empty query should return 
        self.assertEqual(user.query({}),
         user.parseFile())
        self.assertEqual(user.query({
            "name":"guest",
            "home":"/home/guest",
            "uid":"100",
            "gid":"100"
        }),[{"name": "guest", "encryption": "!", "uid": "100", "gid": "100", "comment": "", "home": "/home/guest", "shell": ""}])
        self.assertEqual(user.query({
            "name":"does not exist",
            "home":"/home/guest",
            "uid":"100",
            "gid":"100"
        }),[])
        
class GroupTestCase(TestCase):
    def testQuery(self):
        group = Group()
