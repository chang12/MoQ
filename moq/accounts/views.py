from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import login as auth_login
from django.shortcuts import redirect, render

# Create your views here.


def login(request):
    return auth_login(request)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:index')

    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', {
        'form': form,
    })


@login_required
def profile(request):
    user = request.user
    group_list = user.group_set.all()
    question_list = user.question_set.all()
    answer_list = user.answer_set.all()
    return render(request, 'accounts/profile.html', {
        'group_list': group_list,
        'question_list': question_list,
        'answer_list': answer_list,
    })
