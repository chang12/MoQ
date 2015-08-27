from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from blog.forms import GroupForm, QuestionForm, AnswerForm
from blog.models import Group, Question, Answer

# Create your views here.


def index(request):
    return render(request, 'blog/index.html')


def group_list(request):
    group_list = Group.objects.all()
    return render(request, 'blog/group_list.html', {
        'group_list': group_list,
    })


def group_detail(request, group_pk):
    group = get_object_or_404(Group, pk=group_pk)
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
def group_edit(request, group_pk):
    group = get_object_or_404(Group, pk=group_pk)
    if request.user == group.owner:
        if request.method == 'POST':
            form = GroupForm(request.POST, instance=group)
            if form.is_valid():
                form.save()
                return redirect('blog:group_detail', group_pk)

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
def group_delete(request, group_pk):
    group = get_object_or_404(Group, pk=group_pk)
    if request.user == group.owner:
        group.delete()
        return redirect('blog:index')
    else:
        content = '해당 그룹의 소유자만 삭제할 수 있습니다'
        return render(request, 'blog/error.html', {
            'content': content,
        })


@login_required
def question_detail(request, group_pk, question_pk):
    group = get_object_or_404(Group, pk=group_pk)
    question = get_object_or_404(Question, pk=question_pk)
    answer_list = question.answer_set.all()
    return render(request, 'blog/question_detail.html', {
        'group': group,
        'question': question,
        'answer_list': answer_list,
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


# @login_required
# def answer_detail(request, group_pk, question_pk, answer_pk):
#     group = get_object_or_404(Group, pk=group_pk)
#     question = get_object_or_404(Question, pk=question_pk)
#     answer = get_object_or_404(Answer, pk=answer_pk)
#     return render(request, 'blog/answer_detail.html', {
#         'group': group,
#         'question': question,
#         'answer': answer,
#     })


@login_required
def answer_new(request, group_pk, question_pk):
    question = get_object_or_404(Question, pk=question_pk)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.question = question
            answer.save()
            return redirect('blog:question_detail', group_pk, question_pk)

    else:
        form = AnswerForm()

    return render(request, 'blog/form.html', {
        'form': form,
    })


@login_required
def answer_edit(request, group_pk, question_pk, answer_pk):
    answer = get_object_or_404(Answer, pk=answer_pk)
    if answer.author == request.user:
        if request.method == 'POST':
            form = AnswerForm(request.POST, instance=answer)
            if form.is_valid():
                form.save()
                return redirect('blog:answer_detail', group_pk, question_pk, answer_pk)
        else:
            form = AnswerForm(instance=answer)
        return render(request, 'blog/form.html', {
            'form': form,
        })

    else:
        content = '해당 답변의 작성자가 아닙니다.'
        return render(request, 'blog/error.html', {
            'content': content,
        })


@login_required
def answer_delete(request, group_pk, question_pk, answer_pk):
    answer = get_object_or_404(Answer, pk=answer_pk)
    if answer.author == request.user:
        answer.delete()
        return redirect('blog:question_detail', group_pk, question_pk)
    else:
        content = '해당 답변의 작성자가 아닙니다.'
        return render(request, 'blog/error.html', {
            'content': content,
        })
