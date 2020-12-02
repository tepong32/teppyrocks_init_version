from django.db import models
from django.utils import timezone	# for "default" argument in DateTimeField
from django.contrib.auth.models import User
from django.urls import reverse

from django.utils.safestring import mark_safe
from markdown_deux import markdown

class BlogPost(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted = models.DateTimeField(auto_now_add=True) #you can use "(default=timezone.now)" instead but the timezone import is needed
	date_modified = models.DateTimeField(auto_now=True) # shows the actual time the post was modified // everytime it is modified
	# # for displaying the date_modified field only when posts get modified
	# modified = models.BooleanField(default=False)
	# if date_modified != date_posted:
	# 	modified = models.BooleanField(default=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE) # ForeignKey is for relationship with another model

	# tag-picker options
	Entertainment = "Entertainment"
	Help = "Help!"
	Hobby = "Hobby"
	Jokes = "Jokes"
	School = "School"
	Social = "Social"
	Tech = "Tech"

	post_tags = [
		(Entertainment, "Entertainment"),
		(Help, "Help!"),
		(Hobby, "Hobby"),
		(Jokes, "Jokes"),
		(School, "School"), # should be further categorized into below:
			# (
		# 	('Coding': 'Coding'),
		# 	('Art': 'Art'),
		# 	('Math': 'Math'),
		# 	('Science': 'Science'),
		# 	('Language': 'Language')
		# 	),
		(Social, "Social"),
		(Tech, "Tech")
	]
	tag = models.CharField(
		max_length=15,
		choices=post_tags,
		default=Social,
	)
	# additional options for tag to categorize Help
	# if tag == Help:
	# 	General = "General Info"
	# 	Code = "Code"
	# 	Tech = "Tech"
	# 	helpfor_choices = [
	# 		(General, "General Info"),
	# 		(Code, "Code"),
	# 		(Tech, "Tech")
	# 	]

	# 	helpfor = models.CharField(max_length=10,
	# 		choices=helpfor_choices,
	# 		default=General
	# 	)


	def __str__(self):			# for printing the title of the post whenever it gets called in the query (using python shell)
		return self.title

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

	def get_markdown(self):
		content = self.content
		markdown_text = markdown(content)
		return mark_safe(markdown_text)


# not being used atm // not working
class BlogComment(models.Model):
	post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, default=1)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	#title = BlogPost.title
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True) #you can use "(default=timezone.now)" instead but the timezone import is needed
	date_modified = models.DateTimeField(auto_now=True) # shows the actual time the post was modified // everytime it is modified

	def __str__(self):			# for printing the title of the post whenever it gets called in the query (using python shell)
		return "{}-{}".format(self.post.title, str(self.user.username))

	# def get_absolute_url(self):
	# 	return reverse('post-detail', kwargs={'pk': self.pk})

	def get_markdown(self):
		content = self.content
		markdown_text = markdown(content)
		return mark_safe(markdown_text)
