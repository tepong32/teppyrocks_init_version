from django.db import models
from django.utils import timezone	# for "default" argument in DateTimeField
from django.contrib.auth.models import User
from django.urls import reverse


class ToDoList(models.Model):
	'''
	a list of things to be done on/before a specific date
	'''
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	
	Random = "Random"
	Home = "Home"
	School = "School"
	Work = "Work"
	Hobby = "Hobby"
	category_choices=[
		(Home, "Home"),
		(School, "School"),
		(Work, "Work"),
		(Hobby, "Hobby"),
	]
	category = models.CharField(
		max_length=15,
		choices=category_choices,
		default=Random)

	desc = models.CharField(max_length=300)
	status = models.BooleanField(default=False)
	date_created = models.DateTimeField(auto_now_add=True)
	finish_by = models.DateField(auto_now_add=False)		# deadline
	# finish_by should be a date selector, JS widget maybe?

	def __str__(self):
		return self.category

	def get_absolute_url(self):
		return reverse('todo-detail', kwargs={'pk': self.pk})


# not making any sense // not being used atm
class ToDoItems(models.Model):
	name = models.CharField(max_length=100)
	category = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

	def __str__(self):
		return self.name


