from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

class PasswordDatabase(models.Model):
    db_name=models.CharField(max_length=50)
    db_password=models.CharField(max_length=50,null=False)
    db_user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    db_slug = AutoSlugField(populate_from='db_name',unique=True, null=True, default=None)
# Create your models here.
