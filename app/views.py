from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def paginate(objects_list, request, per_page=10):
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
    questions = []
    for i in range(1, 31):
        questions.append({
            'id': i,
            'title': f'Как стать сигмой? {i}',
            'text': f',бла бла бла бла...хочу стать сигмой {i}.',
            'rating': i,
            'tags': ['Общество', 'Наука', 'Культура']
        })
    page = paginate(questions, request)
    context = {
        'questions': page.object_list,
        'page': page
    }
    return render(request, 'index.html', context)


def hot(request):
    # создаём те же вопросы, но отсортированные по рейтингу
    questions = []
    for i in range(1, 31):
        questions.append({
            'id': i,
            'title': f'Горячий вопрос {i}',
            'text': f' горячий вопрос текст {i}.',
            'rating': i,
            'tags': ['Новости', 'Спорт']
        })
    page = paginate(questions, request)
    context = {
        'questions': page.object_list,
        'page': page
    }
    return render(request, 'hot.html', context)


def tag(request, tag):
    questions = []
    for i in range(1, 30):
        questions.append({
            'id': i,
            'title': f'Вопрос {i}',
            'text': f'тема {tag}, вопрос номер {i}.',
            'rating': i,
            'tags': [tag, 'Наука']
        })

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
    question = {
        'id': question_id,
        'title': f'Как стать сигмой? #{question_id}',
        'text': 'бла бла бла бла... как стать сигмой',
        'rating': 15,
        'tags': ['Общество', 'Спорт'],
        'answers': [
            {'author': 'Мария', 'text': 'Ответ'},
            {'author': 'Павел', 'text': 'Более крутой ответ'},
            {'author': 'Алексей', 'text': 'Ты Годжо сатору потому что ты сигма, или ты сигма, потому что ты Годжо Сатору?'},
        ]
    }

    context = {'question': question}
    return render(request, 'question.html', context)


def register(request):
    return render(request, 'register.html')


def settings(request):
    return render(request, 'settings.html')
