from django.forms import ModelForm
from blog.models import Group, Question, Answer


class GroupForm(ModelForm):
    class Meta:
        model = Group
        exclude = ('owner', )


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        exclude = ('author', 'group', )


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        exclude = ('author', 'question', )
