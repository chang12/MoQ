from django.forms import ModelForm
from blog.models import Group, Question


class GroupForm(ModelForm):
    class Meta:
        model = Group
        exclude = ('owner', )


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        exclude = ('author', 'group', )
