from django.db import models
from django.contrib.auth.models import User

# Create notebook model
class Notebook(models.Model):
    # Add a foreign key to the user model
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notebooks')
    title = models.CharField(max_length=200, blank=False)
    content = models.TextField(blank=True, default="___________")  # The content can be left empty
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} written by {self.user.username}"