from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Question


def paginate(objects_list, request, per_page=20):
    paginator = Paginator(objects_list, per_page)
    page_num = request.GET.get('page', 1)
    try:
        page = paginator.page(page_num)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page

def index(request):
    questions = Question.objects.new()
    page = paginate(questions, request)
    context = {
        'questions': page.object_list,
        'page': page
    }
    return render(request, 'index.html', context)


def hot(request):
    # создаём те же вопросы, но отсортированные по рейтингу
    questions = Question.objects.best()
    page = paginate(questions, request)
    context = {
        'questions': page.object_list,
        'page': page
    }
    return render(request, 'hot.html', context)


def tag(request, tag):
    questions = Question.objects.tag(tag)
    page = paginate(questions, request)
    context = {
        'tag_name': tag,
        'questions': page.object_list,
        'page': page
    }
    return render(request, 'tag.html', context)


def ask(request):
    return render(request, 'ask.html')


def login(request):
    return render(request, 'login.html')


def question(request, question_id):
    # "рыба" — один вопрос с ответами
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'question.html', context)


def register(request):
    return render(request, 'register.html')


def settings(request):
    return render(request, 'settings.html')
