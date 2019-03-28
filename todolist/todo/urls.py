from django.urls import path
from .views import todolist_view,add_task,make_complete,make_uncomplete,remove_completed_task,delete_task,get_login,edit_task

urlpatterns = [
    path('',todolist_view,name='list'),
    path('add/',add_task, name='add'),
    path('login/',get_login, name='login'),
    path('make_complete/',make_complete,name="mark"),
    path('make_uncomplete/',make_uncomplete,name="unmark"),
    path('remove_completed/',remove_completed_task,name="remove"),
    path('delete_task/',delete_task,name="delete"),
    path('edit_task/',edit_task,name="edit"),
]