from django.contrib import admin

from .models import Book, Author, AuthorDescription
# Register your models here.

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(AuthorDescription)

