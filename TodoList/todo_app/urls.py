from django.urls import path
from . import views
from accounts import views as view

urlpatterns = [
    path('', views.index, name='index'),
    path('list/<str:date>', views.todo_list, name='todo_list'),
    path('post/', views.todo_post, name='todo_post'),
    path('edit/<int:pk>', views.todo_edit, name='todo_edit'),
    path('done/<int:pk>', views.todo_done, name='todo_done'),
    path('delete/<int:pk>', views.todo_delete, name='todo_delete'),
    path('detail/<int:pk>', views.todo_detail, name='todo_detail'),
    path('today', views.todo_today, name='todo_today'),
]