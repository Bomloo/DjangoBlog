from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, "articles/article_list.html", {"articles": articles})

def article_details(request, slug):
    # we receive the slug from the url, now we want to use the slug to pull
    # appropriate model from database

    # from all article objects, we get the one that matches the slug we receive
    article = Article.objects.get(slug = slug)
    # we render an html templates
    # we pass request
    # we pass file location to grab the template
        # settings marks program to search all template folders
        # we want to grab the one name spaced with articles_list
    # we send info to html in dictionary format
    return render(request, "articles/article_details.html", {"article": article})
