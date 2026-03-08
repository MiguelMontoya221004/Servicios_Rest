from django.urls import path
from . import views


urlpatterns = [
    path('todos/', views.TodoListCreate.as_view(), name='list'),
    path('todos/<int:pk>', views.TodoRetrieveUpdateDestroy.as_view(), name='todo_RUD'),
    path('todos/<int:pk>/complete', views.TodoToggleComplete.as_view(), name='todo_toggle_complete'),
]
