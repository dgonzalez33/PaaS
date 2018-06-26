from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import User, Group
import json
def index(request):
    """ Default method for when a url is not matched """
    badRequest("Url not found")

def all_users(request):
    """ Display all users as json. """
    user = User()
    return HttpResponse(json.dumps(user.parseFile()))
def query_users(request):
    """ Query users based on the GET parameters. Display in json format.
        Only the following parameters are allowed: """
    if(any(param not in ["name",'encryption',"uid","gid","comment","home","shell"]  for param in request.GET)):
        badRequest("Parameters incorrect")
    user = User()
    return HttpResponse(json.dumps(user.query(request.GET)))
def users_by_uid(request, uid):
    """ Display a user in json format based on its user id. """
    user = User()
    user = user.query({"uid":str(uid)})
    if(len(user) == 0):
        badRequest("No user for the given uid")
    return HttpResponse(json.dumps(user))
def groups_by_uid(request, uid):
    """ Display in json the group found from the given user id. """
    user = User()
    users = user.query({"uid":str(uid)})
    if(len(users) < 1):
        return HttpResponse("No user found under uid "+ str(uid))
    group = Group()
    group = group.query({"gid":str(users[0]['gid'])})
    if(len(group) < 1):
        return HttpResponse("No group found under uid "+ str(uid))
    return HttpResponse(json.dumps(group))
def all_groups(request):
    """ Display in json all of the groups available. """
    group = Group()
    return HttpResponse(json.dumps(group.parseFile()))
def query_groups(request):
    """ Query groups based on the GET parameters. Display in json format.
        Only the following parameters are allowed: """
    if(any(elem not in ["name","password","gid","member"]  for elem in request.GET)):
        badRequest("Parameters incorrect")
    group = Group()
    # Must format params to allow for multiple members under same key. Dict converts all to arrays, rest is converted back.
    params = dict(request.GET)
    for key in params.keys():
        if(key != "member"):
            params[key] = params[key][0]
    return HttpResponse(json.dumps(group.query(params)))
def groups_by_id(request, gid):
    """ Display a group from the given group id. """
    group = Group()
    filtered_groups = group.query({"gid":str(gid)})
    if len(filtered_groups) == 0:
        badRequest("No available group under GID "+str(gid))
    return HttpResponse(json.dumps(filtered_groups))
def badRequest(message):
    """ Display a 404 page with a given message after any bad request. """
    raise Http404(message)