from django import forms
from captcha.fields import CaptchaField

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment"
        })
    )
    captcha = CaptchaField(
        label="What does this say?",
        required=True,
    )    