# imports
from django import forms
from .models import Post


# to create new posts
class NewPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'body', 'topics')


# to edit old posts
class EditPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'body', 'topics')

