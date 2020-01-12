from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
	mob_no = models.IntegerField()
	following = models.ManyToManyField("self", related_name='followers', blank=True, symmetrical=False)
	# topics you like to know abt foriegn key
	# topics you know fk


	def __str__(self):
		return self.user.email


