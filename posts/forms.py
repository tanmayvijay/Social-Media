from django import forms
from .models import Post

class NewPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'body', 'topics')



# class EditPostForm(forms.Form):
# 	title = forms.CharField()
# 	body = forms.TextField()


class EditPostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'body', 'topics')

