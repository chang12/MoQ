from django.shortcuts import HttpResponse, render
from django.views.decorators.csrf import csrf_exempt
from comm.forms import PostForm
from comm.models import Post

# Create your views here.


# @csrf_exempt
# def index(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Thank you for your posting\n")
#     else:
#         form = PostForm()
#         post_list = Post.objects.all()

#     return render(request, 'comm/index.html', {
#         'form': form,
#         'post_list': post_list,
#     })


@csrf_exempt
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
