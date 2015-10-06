from django.shortcuts import HttpResponse
from comm.forms import PostForm

# Create your views here.


def index(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            response = HttpResponse("This response is for POST request\n")

    else:
        response = HttpResponse("This response is for GET request\n")

    return response
