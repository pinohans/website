from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Solvedata(models.Model):
    user = models.OneToOneField(User)
    class Meta:
        permissions = (
            ("solve_data", "Can solve data"),
        )
class Func1(models.Model):
    user = models.OneToOneField(User)
    class Meta:
        permissions = (
            ("func1", "Can use func1"),
        )
class Func2(models.Model):
    user = models.OneToOneField(User)
    class Meta:
        permissions = (
            ("func2", "Can use func2"),
        )
