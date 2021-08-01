from django.urls import path, include

from . import views

app_name = 'bestbooks'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/book/', views.Detail_Book_View.as_view(), name='book_detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('authors/', views.authors_list, name='authors_list'),

]