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
    return HttpResponse(slug)
