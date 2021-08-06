from django import forms
from .models import Comment, Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'description', 'published_date', 'author')


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('book', 'comment_text')


