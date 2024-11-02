from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    rating = models.IntegerField(default=5)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Feedback from {self.user.username} at {self.timestamp}'
