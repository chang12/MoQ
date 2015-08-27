from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from blog.forms import GroupForm
from blog.models import Group

# Create your views here.


def index(request):
    group_list = Group.objects.all()
    return render(request, 'blog/index.html', {
        'group_list': group_list,
    })


def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)
    return render(request, 'blog/group_detail.html', {
        'group': group,
    })


@login_required
def group_new(request):
    if request.method == "POST":
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.owner = request.user
            group.save()
            return redirect('blog:index')

    else:
        form = GroupForm()

    return render(request, 'blog/form.html', {
        'form': form,
    })


@login_required
def group_edit(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.user == group.owner:
        if request.method == 'POST':
            form = GroupForm(request.POST, instance=group)
            if form.is_valid():
                form.save()
                return redirect('blog:group_detail', pk)

        else:
            form = GroupForm(instance=group)

        return render(request, 'blog/form.html', {
            'form': form,
        })

    else:
        content = '해당 그룹의 소유자가 아닙니다'
        return render(request, 'blog/error.html', {
            'content': content,
        })


@login_required
def group_delete(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.user == group.owner:
        group.delete()
        return redirect('blog:index')
    else:
        content = '해당 그룹의 소유자만 삭제할 수 있습니다'
        return render(request, 'blog/error.html', {
            'content': content,
        })
