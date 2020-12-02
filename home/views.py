from django.shortcuts import render
from .models import SubAnnouncement 	# this model is not being used. maybe change it as Announcements
from todo.models import ToDoList
from blog.models import BlogPost
from django.contrib.auth.models import User
from django.core.paginator import Paginator



def landing(request):
	# For accessing just the "<domain_name>/" even when the user is automatically logged-in.
	# Default will be an announcements/advertisements page.
	# "<domain_name>/home" will be the homepage linked with the "home" icon; not this one.
	user = User
	context = {
		'subannouncements': SubAnnouncement.objects.all(),
		'users': user.objects.order_by('-date_joined'), # try 'date_registered' to see all options
		# 'ads': 
	}
	if user:
		return render(request, 'home/wb.html', context)
	else:
		return render(request, 'home/_home.html', context)



from django.contrib.auth.decorators import login_required

@login_required
def home(request):
	user = User
	user_list = User.objects.all()
	#paginator = Paginator(user_list, 10) # not yet implemented
	context = {
		'todos': ToDoList.objects.filter(author=request.user).order_by("finish_by"),
		'blogposts': BlogPost.objects.all().order_by("-date_posted"),
		'users': user_list
	}

	# template_folder/html_file
	return render(request, 'home/home.html', context)











def announcement(request):
	# not being used atm
	context = {

	}

	return render(request, 'home/test.html', context)


# as the name suggests, this page is just for testing how html+logic works...if they do.
def testing(request, username=None):
	user_list = User.objects.all()
	context = {
		'announcements': SubAnnouncement.objects.all(), # not being used // no instance created for this
		'todos': ToDoList.objects.filter(author=request.user).order_by("finish_by"),
		'blogposts': BlogPost.objects.all().order_by("-date_posted"),
		'users': user_list
	}
	return render(request, 'home/test.html')