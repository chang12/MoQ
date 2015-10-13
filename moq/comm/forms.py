from django.forms import ModelForm
from comm.models import Location, Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = '__all__'
