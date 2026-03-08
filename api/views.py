from rest_framework import generics, permissions
from .serializers import ToDoSerializer
from todo.models import ToDo


class TodoListCreate(generics.ListCreateAPIView):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all().order_by('-created')
    permission_classes = [permissions.IsAuthenticated]
    
class TodoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ToDo.objects.filter(user=user)

