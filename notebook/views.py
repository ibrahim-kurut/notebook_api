
from rest_framework import viewsets
from .models import Notebook
from .serializers import NotebookSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner

class NotebookViewSet(viewsets.ModelViewSet):
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer
    permission_classes = [IsAuthenticated, IsOwner]  # Make sure that the user is registered

    def get_queryset(self):
        """
        It only displays the notes that the current user has.
        """
        return Notebook.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  #Save the current user as an owner of the note