from django.urls import path
from . import views

urlpatterns = [
    path('tasks', views.TaskView.as_view()),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view()),

    path('lists', views.ListView.as_view()),
    path('lists/<int:pk>/', views.ListDetailView.as_view()),

    path('groups', views.GroupView.as_view()),
]