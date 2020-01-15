#imports
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# user profile model
class UserProfile(models.Model):
	# each profile is related to a user field
	user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
	mob_no = models.IntegerField()
	following = models.ManyToManyField("self", related_name='followers', blank=True, symmetrical=False)

	# string representation of user profile
	def __str__(self):
		return self.user.email


