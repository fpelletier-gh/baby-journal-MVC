from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Baby
from .models import Post


class BabyForm(forms.ModelForm):
    class Meta:
        model = Baby
        fields = ["text"]
        labels = {"text": ""}


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["text"]
        labels = {"text": ""}
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}
