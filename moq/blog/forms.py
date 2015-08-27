from django.forms import ModelForm
from blog.models import Group


class GroupForm(ModelForm):
    class Meta:
        model = Group
        exclude = ('owner', )
