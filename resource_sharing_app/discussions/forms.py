from django import forms
from .models import Comment,Discussion

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class CreateDiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ['discussion_id', 'title']