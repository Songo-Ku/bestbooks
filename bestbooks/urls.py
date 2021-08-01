from django.urls import path, include

from . import views

app_name = 'bestbooks'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('authors/', views.authors_list, name='authors_list'),

]