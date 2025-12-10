from django.db import models

# Create your models here.


class Book(models.Model):
    author_name = models.CharField(max_length=100)
    book_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return f"{self.book_name}"
