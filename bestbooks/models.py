from django.db import models
from django.utils import timezone
import datetime

class Author(models.Model):
    author_fl = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    # books =

    def __str__(self):
        return self.author_fl

    def was_published_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)

#      should be here method to response all books per author


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField('date published')
    # models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title