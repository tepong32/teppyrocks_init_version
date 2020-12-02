from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django import forms
# from PIL import Image


# pag-isipan mo pa kung mag-allow ng space-consuming uploads such as mp3s
# here's the abstract of the model if yes:

# class LoungeSounds(models.Model):
# 	title = models.CharField(max_length=100)
# 	desc = models.CharField(widget=models.Textarea())

# 	# copy and modify this func for other uploadable classes
# 	def sound_directory_path(instance, filename):
# 		# file will be uploaded to MEDIA_ROOT/user_<username>/<filename>
# 		return '{0}/sounds/{1}'.format(instance.user.username, filename)

# 	upload = models.FileField(upload_to=sound_directory_path)	# add validation methods for uploads
# 	owner = models.ForeignKey(User, on_delete=models.CASCADE)
# 	date_uploaded = models.DateTimeField(auto_now_add=True)

# 	def __str__(self):
# 		return self.title

# 	def get_absolute_url(self):
# 		return reverse('lounge-sounds', kwargs={'pk': self.pk})


class LoungeUnsentLetters(models.Model):
	title = models.CharField(max_length=100)
	letter_for = models.CharField(max_length=100)
	message = models.CharField(max_length=3000)
	attach_file = models.BooleanField(default=False)
	date_posted = models.DateTimeField(auto_now_add=True)
	# author should not be shown publicly and just used for tracking/tracing by admins
	author = models.ForeignKey(User, on_delete=models.CASCADE) 

	def unsentletters_directory_path(instance, filename):
		# file will be uploaded to MEDIA_ROOT/user_<username>/<filename>
		return 'unsent_letters/{}/{}'.format(instance.user.username, filename)

	# do not forget to add validation methods for uploads (security reasons)
	# seems like this should be a method as the if statement is not showin on forms.py
	# when attach_file = True
	if attach_file == True:
		upload = models.FileField(upload_to=unsentletters_directory_path)
		upload_date = models.DateTimeField(auto_now_add=True)


	

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('lounge-ul-detail', kwargs={'pk': self.pk})