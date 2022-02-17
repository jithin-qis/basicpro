from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=20)
    price = models.IntegerField()
    image = models.FileField(upload_to='product pics')
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title