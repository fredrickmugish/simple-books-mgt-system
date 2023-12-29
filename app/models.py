from django.db import models

# Create your models here.

class Book(models.Model):
   
    title=models.CharField(max_length=40)
    price=models.CharField(max_length=10)

    def __str__(self):
        return f"Title: {self.title}, Price: {self.price}"
        
    