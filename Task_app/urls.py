from django.urls import path
from . import views
urlpatterns=[
    path('', views.login, name='login'),     #it will make a form where user can login or signup
    path('signup', views.signup, name='signup'),
    path('homepage', views.homepage, name='homepage'),
    path('logout', views.logout, name='logout'),
    path('add_task', views.add_task, name='add_task'),
    path('update_task_status', views.update_task_status, name='update_task_status'),

]