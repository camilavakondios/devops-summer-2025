from django.db import models

class Book(models.Model):
    isbn = models.CharField(max_length=17, unique=True, null=False)
    title = models.CharField(max_length=225)
    description = models.TextField(blank=True)
    author = models.CharField(max_length=255)
    published_date = models.DateField() #Stores a date (YYYY-MM-DD)
    created_at = models.DateTimeField(auto_now=True)
    
