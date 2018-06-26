from django.urls import path, re_path

from . import views

urlpatterns = [
    path('users/', views.all_users, name='all_users'),
    re_path('users/query/$', views.query_users, name='query_users'),
    path('users/<int:uid>', views.users_by_uid, name='users_by_uid'),
    path('users/<int:uid>/groups', views.groups_by_uid, name='groups_by_uid'),
    path('groups/', views.all_groups, name='all_groups'),
    re_path('groups/query/$', views.query_groups, name='query_groups'),
    path('groups/<int:gid>', views.groups_by_id, name='groups_by_id'),
    re_path('$', views.index, name='index')
]