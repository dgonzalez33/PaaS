from django.test import TestCase
from .models import User, Group
class UserTestCase(TestCase):
    def testQuery(self):
        user = User("testpasswd")
        #Empty query should return all the users
        self.assertEqual(user.query({}),
         user.parseFile())
        #testing query for name, uid, and gid.
        self.assertEqual(user.query({
            "name":"guest",
            "home":"/home/guest",
            "uid":"100",
            "gid":"100"
        }),[{"name": "guest", "uid": "100", "gid": "100", "comment": "", "home": "/home/guest", "shell": ""}])
        #Testing a name that does not exist.
        self.assertEqual(user.query({
            "name":"does not exist",
            "home":"/home/guest",
            "uid":"100",
            "gid":"100"
        }),[])
        
class GroupTestCase(TestCase):
    def testQuery(self):
        group = Group("testgroup")
        self.assertEqual(group.query({}),
         group.parseFile())
        self.assertEqual(group.query({
            "name":"staff",
            "gid":"1",
            "member":["shadow","cjf"]
        }),[{"name": "staff", "gid": "1", "members": ["shadow", "cjf"]}])
        self.assertEqual(group.query({
            "name":"does not exist",
            "gid":"1"
        }),[])

