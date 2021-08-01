from django.db import models
from django.utils import timezone
import datetime


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def was_published_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)

#      should be here method to response all books per author


# class AuthorDescription:
#     # napisać sygnał gdy dodaje kolejna ksiazke dla autora zeby weryfikował czy books written sie nie powinno zmienić
#     BOOKS_WRITTEN = (
#         ('s', 'less than 5 books'),
#         ('m', 'less or equal 30'),
#         ('h', 'more than 30'),
#     )
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)
#     birthday = models.DateField(null=True, blank=True)
#     books_written = models.CharField(max_length=1, choices=BOOKS_WRITTEN)
#     youtube_url = models.URLField(null=True, blank=True)
#
#     def calculate_age(self):
#         import datetime
#         return int((datetime.datetime.now() - self.birthday).days / 365.25)
#     age = property(calculate_age)
#     # < span > Age: {{person.age | timesince}} < / span > ciekawostka zeby nie trzeba bylo robic tutaj obliczen


class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField('date published')
    # models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

