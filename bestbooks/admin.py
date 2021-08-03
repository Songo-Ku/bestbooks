from django.contrib import admin

from .models import Book, Author, AuthorDescription
# Register your models here.

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(AuthorDescription)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

