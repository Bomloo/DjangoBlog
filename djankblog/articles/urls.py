from django.urls import path
# . means in same directory
# we import views to access the function for handling a url call
from . import views

# we use this to name space url path names
app_name = "articles"

urlpatterns = [
    # when blank we call articles_list function in views to display all articles
    path("", views.article_list, name = "list"),
    # <str:<name>> will capture portion within string and send it to a parameter
    # called <name> in views.<method>
    path("<str:slug>/", views.article_details, name = "details"),
]
