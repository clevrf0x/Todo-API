from django.urls import path
from . import views

urlpatterns = [
  path('', views.apiOverview, name='api-overview'),
  path('task-list/', views.taskList, name='task-list'),
  path('task-view/<str:id>/', views.taskView, name='task-view'),
  path('task-create/', views.taskCreate, name='task-create'),
  path('task-update/<str:id>/', views.taskUpdate, name='task-update'),
  path('task-delete/<str:id>/', views.taskDelete, name='task-delete'),
  path('task-progress/', views.taskProgress, name='task-progress'),
  path('task-completed/', views.taskCompleted, name='task-completed')
]