"""
URL configuration for djankblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# . means in same directory
# we import views to access the function for handling a url call
from . import views

urlpatterns = [
    # ^ means anything after must be beginning of string
    # $ means anything before will be the end
    path("admin/", admin.site.urls),
    # begin with about/ and end
    # when someone requests the about url, we fire the about function from views
    path("about/", views.about),
    # blank after address.com/, begin and end with nothing
    path("", views.homepage),
]
