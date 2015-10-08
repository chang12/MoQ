from django.shortcuts import HttpResponse, render
from comm.forms import PostForm
from comm.models import Post

# Create your views here.


def index(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            response = HttpResponse("This response is for POST request\n")

    else:
        post_list = Post.objects.all()
        response = render(request, 'comm/index.html', {
            'post_list': post_list,
        })

    return response
