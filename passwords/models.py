from django.db import models
from passwordDatabase.models import PasswordDatabase
class Password(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    password_db = models.ForeignKey(PasswordDatabase, null=False, on_delete=models.CASCADE)

# Create your models here.
