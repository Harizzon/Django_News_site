from django.shortcuts import render
from django.http import HttpResponse
# from django.template import RequestContext

# index page


def index(request):
    return render(request, 'articles/index.html')

# Article section


def articles(request):
    return render(request, 'articles/article.html')


def num_article(request, article_id):
    return HttpResponse(f'Article with number {article_id}')


def archive(request):
    return render(request, 'articles/archive.html')


def num_archive(request, article_id):
    return HttpResponse(f'Article from archive with number {article_id}')

# User section


def users(request):
    return render(request, 'articles/users.html')


def num_users(request, user_id):
    return HttpResponse(f'This is user\'s page number: {user_id}')




