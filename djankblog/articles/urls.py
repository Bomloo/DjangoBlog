from django.urls import path
# . means in same directory
# we import views to access the function for handling a url call
from . import views

urlpatterns = [
    # when blank we call articles_list function in views to display all articles
    path("", views.article_list)
]
