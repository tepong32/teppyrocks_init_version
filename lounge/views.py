from django.shortcuts import render, get_object_or_404
from .models import LoungeUnsentLetters
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
from .forms import ULForm


class LoungeListView(ListView):
	model = LoungeUnsentLetters
	context = {'u_letters': LoungeUnsentLetters.objects.all()}
	context_object_name = 'u_letters'
	template_name = 'lounge/lounge_home.html'	
	ordering = ['-date_posted']
	paginate_by = 3


# class UserToDoListView(ListView):
# 	model = BlogPost 			
# 	template_name = 'blog/blog_userposts.html'
# 	context_object_name = 'posts'		# getting the 'posts' key from "context = {'posts': Post.objects.all(),}"
# 	ordering = ['-date_posted']
# 	paginate_by = 5	

# 	def get_queryset(self):		# this defines the filter for the specific user's posts
# 		user = get_object_or_404(User, username=self.kwargs.get('username'))
# 		return BlogPost.objects.filter(author=user).order_by('-date_posted')



class LoungeDetailView(LoginRequiredMixin, DetailView):
	model = LoungeUnsentLetters
	template_name = 'lounge/lounge_ul_detail.html'
	post = LoungeUnsentLetters.objects.all()
	context = {'u_letters': LoungeUnsentLetters.objects.all()}


#from .forms import ToDoForm
class LoungeCreateView(LoginRequiredMixin, CreateView):		
	model = LoungeUnsentLetters
	context = {'u_letters': LoungeUnsentLetters.objects.all()}
	context_object_name = 'u_letters'
	form_class = ULForm
	template_name = 'lounge/lounge_ul_form.html'

	def form_valid(self, form):			#to automatically get the id of the current logged-in user as the author
		form.instance.author = self.request.user 	#set the author to the current logged-in user
		return super().form_valid(form)


class LoungeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = LoungeUnsentLetters 
	form_class = ULForm
	template_name = 'lounge/lounge_ul_form.html'

	# def form_valid(self, form):			
	# 	form.instance.author = self.request.user 
	# 	return super().form_valid(form)

	def test_func(self):
		ul = self.get_object()

		if self.request.user == ul.author:
			return True
		return False


class LoungeDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):		
	model = LoungeUnsentLetters
	context = {'u_letters': LoungeUnsentLetters.objects.all()}
	context_object_name = 'u_letters'
	template_name = 'lounge/lounge_ul_confirmdelete.html'
	success_url = '/lounge/'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		ul = self.get_object()

		if self.request.user == ul.author:
			return True
		return False		

