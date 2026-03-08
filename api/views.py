from rest_framework import generics, permissions
from .serializers import ToDoSerializer
from todo.models import ToDo


class TodoListCreate(generics.ListCreateAPIView):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all().order_by('-created')
    permission_classes = [permissions.IsAuthenticated]
