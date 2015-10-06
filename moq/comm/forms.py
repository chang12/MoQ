from django.forms import ModelForm
from comm.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
