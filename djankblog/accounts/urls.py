from django.urls import path
# . means in same directory
# we import views to access the function for handling a url call
from . import views

# we use this to name space url path names
app_name = "accounts"

urlpatterns = [
    path("signup/", views.signup_view, name = "signup"),
]
