from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from blog.forms import GroupForm, QuestionForm
from blog.models import Group, Question

# Create your views here.


def index(request):
    group_list = Group.objects.all()
    return render(request, 'blog/index.html', {
        'group_list': group_list,
    })


def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)
    question_list = group.question_set.all()
    return render(request, 'blog/group_detail.html', {
        'group': group,
        'question_list': question_list,
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


def question_detail(request, group_pk, question_pk):
    group = get_object_or_404(Group, pk=group_pk)
    question = get_object_or_404(Question, pk=question_pk)
    return render(request, 'blog/question_detail.html', {
        'group': group,
        'question': question,
    })


@login_required
def question_new(request, group_pk):
    group = get_object_or_404(Group, pk=group_pk)
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.group = group
            question.save()
            return redirect('blog:group_detail', group_pk)

    else:
        form = QuestionForm()

    return render(request, 'blog/form.html', {
        'form': form,
    })


@login_required
def question_edit(request, group_pk, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    if question.author == request.user:
        if request.method == 'POST':
            form = QuestionForm(request.POST, instance=question)
            if form.is_valid():
                form.save()
                return redirect('blog:question_detail', group_pk, question_pk)
        else:
            form = QuestionForm(instance=question)
        return render(request, 'blog/form.html', {
            'form': form,
        })

    else:
        content = '해당 질문의 작성자가 아닙니다.'
        return render(request, 'blog/error.html', {
            'content': content,
        })


@login_required
def question_delete(request, group_pk, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    if question.author == request.user:
        question.delete()
        return redirect('blog:group_detail', group_pk)
    else:
        content = '해당 질문의 작성자가 아닙니다.'
        return render(request, 'blog/error.html', {
            'content': content,
        })



