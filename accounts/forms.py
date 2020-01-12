from django import forms
from .models import UserProfile
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Re-Enter Password', widget=forms.PasswordInput)


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', )


	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password1'] != cd['password2']:
			raise forms.ValidationError('Passwords don\'t match!')

		return cd['password2']





class UserProfileForm(forms.ModelForm):

	class Meta:
		model = UserProfile
		fields = ('mob_no',)



class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
