import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):

    CATEGORY_CHOICES = [
        ('Jersey & Apparel', 'Jersey & Apparel'), 
        ('Sepatu Bola', 'Sepatu Bola'), 
        ('Peralatan & Perlengkapan', 'Peralatan & Perlengkapan'), 
        ('Aksesoris & Merchandise', 'Aksesoris & Merchandise'),
       
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=60)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)
    product_views = models.PositiveIntegerField(default=0)
    stock = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
    
    def increment_views(self):
        self.product_views += 1
        self.save()



