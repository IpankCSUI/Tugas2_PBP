from django.urls import path
from todolist.views import create_task, register, login_user, logout_user,show_todolist, show_todolist_json, add_task
 #sesuaikan dengan nama fungsi yang dibuat

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist' ),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create'),
    path('json/', show_todolist_json, name="show_todolist_json"),
    path('add/', add_task, name="add_task"),
]