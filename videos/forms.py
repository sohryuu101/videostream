from django import forms

class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control bg-dark",
            "placeholder": "Leave a Comment!"
        }))