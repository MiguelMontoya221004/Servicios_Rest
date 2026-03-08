from rest_framework import generics
from .serializers import ToDoSerializer
from todo.models import ToDo


class ToDoList(generics.ListCreateAPIView):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all().order_by('-created')
