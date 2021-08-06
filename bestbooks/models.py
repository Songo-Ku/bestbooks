from django.db import models
from django.utils import timezone
from django.conf import settings
import datetime


class Author(models.Model):
    first_name = models.CharField (max_length=200)
    last_name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def was_published_recently(self):
        return self.created >= timezone.now() - datetime.timedelta(days=1)

#      should be here method to response all books per author


class Book(models.Model):
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField('date published')
    # models.IntegerField(default=0)
    author = models.ForeignKey('bestbooks.Author', on_delete=models.CASCADE, related_name='books')
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class AuthorDescription(models.Model):
    # napisać sygnał gdy dodaje kolejna ksiazke dla autora zeby weryfikował czy books written sie nie powinno zmienić
    BOOKS_WRITTEN = (
        ('s', 'less than 5 books'),
        ('m', 'less or equal 30'),
        ('h', 'more than 30'),
    )
    COLORS_PERSONAL = (
        ('black', 'black'),
        ('brown', 'brown'),
        ('green', 'green'),
        ('blond', 'blond'),
        ('blue', 'blue'),
    )

    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='personals')
    birthday = models.DateField(null=True, blank=True)
    death_day = models.DateField(null=True, blank=True)
    books_written = models.CharField(max_length=1, choices=BOOKS_WRITTEN)  # help_text = ''
    youtube_url = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    height = models.IntegerField(default=175)
    color_eyes = models.CharField(max_length=5, choices=COLORS_PERSONAL, default='unknown')
    color_hairs = models.CharField(max_length=5, choices=COLORS_PERSONAL, default='unknown')

    def calculate_age(self):
        import datetime
        if self.death_day:
            return int((self.death_day - self.birthday).days / 365.25)
        # print(int((datetime.date.today() - self.birthday).days / 365.25))
        return int((datetime.date.today() - self.birthday).days / 365.25)

    def is_alive(self):
        if self.death_day:
            return False
        return True
    age = property(calculate_age)
    #     # < span > Age: {{person.age | timesince}} < / span > ciekawostka zeby nie trzeba bylo robic tutaj obliczen

    def __str__(self):
        return f'{self.author.first_name} {self.author.last_name} {self.books_written}'


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # approved_comment = models.BooleanField(default=False)
    #
    # def approve(self):
    #     self.approved_comment = True
    #     self.save()

    def __str__(self):
        return self.comment_text





















# tu chcialbym zrobic model ktory bedzie przyjmowal integer miedzy min i max np. dla wzrostu
# class MyIntegerField(models.IntegerField):
#     def __init__(self, *, max_length=None, min_length=None, strip=True, empty_value='', **kwargs):
#         self.max_length = max_length
#         self.min_length = min_length
#         self.strip = strip
#         self.empty_value = empty_value
#         super().__init__(**kwargs)
#         if min_length is not None:
#             self.validators.append(validators.MinLengthValidator(int(min_length)))
#         if max_length is not None:
#             self.validators.append(validators.MaxLengthValidator(int(max_length)))
#         self.validators.append(validators.ProhibitNullCharactersValidator())