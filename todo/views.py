# from django.shortcuts import render
# from django.http import HttpResponseRedirect
# from .models import ToDoList
# from .forms import *

# # Create your views here.


# tried func-based views but...I returned to class-based

# def todo_create(request):
# 	if request.method == "POST":
# 		form = ToDoForm(request.POST) # or ToDoItemForm(request.POST) - not making sense atm
# 		if form.is_valid():
# 			form.instance.author = request.user 
# 			c = form.cleaned_data["category"]
# 			d = form.cleaned_data["desc"]
# 			td = ToDoList(category=c, desc=d)
# 			td.save()
# 			messages.success(request, f"Item successfully added!")

# 		return HttpResponseRedirect("/todo/%i"%td.id)
# 		# this works the same as the site_adminlte_trial/users/views.py.profile_edit (but with variables declared):
# 		# return render(request, "users/profile_detail.html", {"user":user})


# 	else:
# 		form = ToDoForm()
# 	return render(request, 'todo/todo.html', {'form': form})


# def todo_listview(request):
# 	context = {
# 		'todo': ToDoList.objects.all(),
# 		}
# 	return render(request, 'todo/todo_listview.html', context)


# def todo_detail(request, id):
# 	td = ToDoList.objects.get(id=id)

# 	return render(request, 'todo/todo_detail.html', {'td':td})



#########################################################################
from django.shortcuts import render, get_object_or_404
from .models import ToDoList
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
	FormView,
	)
from .forms import ToDoForm, ToDoItemsForm


class ToDoListView(ListView):
	model = ToDoList
	context = {'todos': ToDoList.objects.all()}
	context_object_name = 'todos'
	template_name = 'todo/todo_home.html'	# getting the 'posts' key from "context = {'posts': Post.objects.all(),}"
	ordering = ['finish_by']			# filter for newest post first
	paginate_by = 5					# # of posts to show per page


# class UserToDoListView(ListView):
# 	model = BlogPost 			
# 	template_name = 'blog/blog_userposts.html'
# 	context_object_name = 'posts'		# getting the 'posts' key from "context = {'posts': Post.objects.all(),}"
# 	ordering = ['-date_posted']
# 	paginate_by = 5	

# 	def get_queryset(self):		# this defines the filter for the specific user's posts
# 		user = get_object_or_404(User, username=self.kwargs.get('username'))
# 		return BlogPost.objects.filter(author=user).order_by('-date_posted')



class ToDoDetailView(LoginRequiredMixin, DetailView):
	#model = ToDoList
	template_name = 'todo/todo_detail.html'
	#post = ToDoList.objects.all()
	context = {'items': ToDoList.objects.all()}
	ordering = ['-date_posted']


#from .forms import ToDoForm
class ToDoCreateView(LoginRequiredMixin, CreateView):		
	model = ToDoList
	context = {'todos': ToDoList.objects.all()}
	context_object_name = 'todos'
	form_class = ToDoForm
	template_name = 'todo/todo_form.html'
	success_url = '/home'

	def form_valid(self, form):			#to automatically get the id of the current logged-in user as the author
		form.instance.author = self.request.user 	#set the author to the current logged-in user
		return super().form_valid(form)


class ToDoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = ToDoList 
	form_class = ToDoForm
	template_name = 'todo/todo_form.html'
	success_url = '/home'

	# def form_valid(self, form):			
	# 	form.instance.author = self.request.user 
	# 	return super().form_valid(form)

	def test_func(self):
		td = self.get_object()

		if self.request.user == td.author:
			return True
		return False


class ToDoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):		
	model = ToDoList
	context = {'todos': ToDoList.objects.all()}
	context_object_name = 'todos'
	template_name = 'todo/todo_confirmdelete.html'
	success_url = '/home'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		td = self.get_object()

		if self.request.user == td.author:
			return True
		return False		

