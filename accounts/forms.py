#imports
from django import forms # django forms library
from django.contrib.auth.models import User # django user model
from django.core.exceptions import ValidationError # for email and password validation
from .models import UserProfile # custom model from models.py file

# user registration form
class UserRegistrationForm(forms.ModelForm):
	# custom input fields
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Re-Enter Password', widget=forms.PasswordInput)

	# meta class
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', )

	# to check for password match
	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password1'] != cd['password2']:
			raise forms.ValidationError('Passwords don\'t match!')

		return cd['password2']




# profile registration form
class UserProfileForm(forms.ModelForm):
	# meta class
	class Meta:
		model = UserProfile
		fields = ('mob_no',)


# login form
class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)


# edit profile form
class EditProfileForm(forms.Form):
	username = forms.CharField()
	first_name = forms.CharField()
	last_name = forms.CharField()
	email = forms.EmailField()
	mob_no = forms.IntegerField()


	# to check for unique username
	def clean_username(self):
		username = self.cleaned_data['username']
		if User.objects.filter(username=username).exists():
			raise ValidationError(f'Username: {username} already exists!')

		return username

	# to check for unique email
	def clean_email(self):
		email = self.cleaned_data['email']
		if User.objects.filter(email=email).exists():
			raise ValidationError(f"Email: {email} already exists!")

		return email