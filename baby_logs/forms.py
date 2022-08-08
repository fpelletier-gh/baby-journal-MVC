from django import forms

from .models import Baby
from .models import Post


class DateInput(forms.DateInput):
    input_type = "date"


class DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"


class BabyForm(forms.ModelForm):
    class Meta:
        model = Baby
        fields = ["first_name", "last_name", "date_of_birth"]
        labels = {
            "first_name": "",
            "last_name": "",
            "date_of_birth": "",
        }
        widgets = {
            "date_of_birth": DateInput(),
            "first_name": forms.TextInput(attrs={"placeholder": "First name"}),
            "last_name": forms.TextInput(attrs={"placeholder": "Last name"}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "text", "date_of_event"]
        labels = {"title": "", "text": "", "date_of_event": "Date of the event: "}
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Title"}),
            "text": forms.Textarea(attrs={"cols": 80, "placeholder": "Description"}),
            "date_of_event": DateTimeInput(),
        }
