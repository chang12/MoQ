from django.forms import ModelForm
from blog.models import Group, Question, Answer


class GroupForm(ModelForm):
    class Meta:
        model = Group
        exclude = ('owner', 'likes', )


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        exclude = ('author', 'group', 'likes', )


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        exclude = ('author', 'question', 'likes', )
