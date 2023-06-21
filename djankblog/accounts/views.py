from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup_view(request):
    # check if it is post request
    if request.method == "POST":
        # we access post data that comes with requests
        # fill usercreationform instance with post data
        # instance creation will validify information
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # if form object is valid, we save to the database
            form.save()
            # log user in

            # if the form is finished, we want to redirect to articles:list
            return redirect("articles:list")
    else:

        # create new instance of usercreationform
        form = UserCreationForm()
        # send instance to html template
    return render(request, "accounts/signup.html", {"form": form})
