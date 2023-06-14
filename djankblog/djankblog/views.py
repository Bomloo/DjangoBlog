# we import the response module with allows us to handl requests and respond
from django.http import HttpResponse
# allows us to render an html template in browser
# make sure templates folder is included in settings dir so that program
# will search for the html templates
from django.shortcuts import render

# when accessing /about we want to send back an http response
def about(request):
    # return HttpResponse("about")

    # renders will take in the request and the html template you want to render
    # will look inside templates folder for the html template
    return render(request, "about.html")

def homepage(request):
    # return HttpResponse("homepage")

    # renders will take in the request and the html template you want to render
    # will look inside templates folder for the html template
    return render(request, "homepage.html")
