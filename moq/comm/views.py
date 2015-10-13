from django.shortcuts import HttpResponse, render
from django.views.decorators.csrf import csrf_exempt
from comm.forms import LocationForm, PostForm
from comm.models import Location, Post

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
        # form = PostForm(request.POST)
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            response = HttpResponse("This response is for POST request\n")

    else:
        location_list = Location.objects.all()
        response = render(request, 'comm/index.html', {
            'location_list': location_list,
        })

    return response
