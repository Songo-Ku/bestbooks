from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Author, Book


class IndexView(generic.ListView):
    template_name = 'bestbooks/index.html'
    context_object_name = 'authors_lists'

    def get_queryset(self):
        return Author.objects.all()


class DetailView(generic.DetailView):
    model = Author
    template_name = 'bestbooks/detail.html'
    # Book.objects.filter(pub_date__lte=timezone.now()).exclude(
    #     choice__choice_text__isnull=True).order_by('-pub_date')[:10]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context['object'])
        author = context['object']
        print(author.id)
        print(Book.objects.filter(author__id=author.id))
        context['books'] = Book.objects.filter(author__id=author.id)
        return context
    # author.id
    # self.get_object()

    # def get_queryset(self):
    #     return Author.objects.filter(id=pk)


def results(request, question_id):
    response = 'you are looking at the results of question %s.'
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse('you are voting on question %s.' % question_id)


def authors_list(request):
    authorsList = Author.objects.all()
    return render(request, 'bestbooks/authors_list.html', {'authorsList': authorsList})


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[0:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     print(f'wyswietl question {question}')
#     return render(request, 'polls/detail.html', {'question': question})