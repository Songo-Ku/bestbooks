from django.shortcuts import render, get_object_or_404

from .models import Author, Book

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[0:5]
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    print(f'wyswietl question {question}')
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = 'you are looking at the results of question %s.'
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse('you are voting on question %s.' % question_id)

def authors_list(request):
    authorsList = Author.objects.all()
    return render(request, 'bestbooks/authors_list.html', {'authorsList': authorsList})
