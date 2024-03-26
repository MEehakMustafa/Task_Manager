from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class task(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)  # Assuming None as the default value
    task_name = models.CharField(max_length=100)
    is_done = models.BooleanField(default=False)