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
# add include to include url from other url files
from django.urls import path, include
# . means in same directory
# we import views to access the function for handling a url call
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# static is only used for debug mode file discovery
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # aarlin
    # aarlin.business@gmail.com
    # aaRlinisbusy360
    path("admin/", admin.site.urls),
    path("articles/", include("articles.urls")),
    path("accounts/", include("accounts.urls")),
    # when someone requests the about url, we fire the about function from views
    path("about/", views.about),
    # when blank we fire the homepage function from views
    path("", views.homepage),
]

# we only use django to handle static files in debug model
# (in deployment we should have something like aws handle static files)
# will check if we are in debug mode and append the urls to tell us how to serve up
# our static files
# the append for static files is for depoyment, but will search for local during debug
urlpatterns += staticfiles_urlpatterns()
# the append for media is only suitable for local development
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
