from .models import BlogComment
from django import forms

class CommentForm(forms.ModelForm):
    """
    Comment Form Model for CommentBlog
    """
    class Meta:
        model = BlogComment
        fields = ('body',)