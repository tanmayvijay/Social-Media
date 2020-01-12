from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

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



class EditProfileForm(forms.Form):
	username = forms.CharField()
	first_name = forms.CharField()
	last_name = forms.CharField()
	email = forms.EmailField()
	mob_no = forms.IntegerField()


	def clean_username(self):
		username = self.cleaned_data['username']
		if User.objects.filter(username=username).exists():
			raise ValidationError(f'Username: {username} already exists!')

		return username


	def clean_email(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email=email).exists():
			raise ValidationError(f"Email: {email} already exists!")

		return email