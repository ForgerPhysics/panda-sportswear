import uuid
from django.db import models

class Product(models.Model):

    # CATEGORY_CHOICES = [
       
    # ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama = models.CharField(max_length=60)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=30)
    is_featured = models.BooleanField()
