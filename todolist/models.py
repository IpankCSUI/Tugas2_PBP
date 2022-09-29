from django.db import models
from django.contrib.auth.models import User
from  django.utils import timezone
# Create your models here.

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE);
    date = models.DateField(default = timezone.now);
    title = models.CharField(max_length=255);
    description = models.TextField();
    is_finished = models.BooleanField(default=False);

    def __str__(self) :
        return self.title