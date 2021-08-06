from django.contrib import admin

from .models import Book, Author, AuthorDescription, Comment
# Register your models here.

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(AuthorDescription)
admin.site.register(Comment)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass



