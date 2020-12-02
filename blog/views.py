from django.shortcuts import render, get_object_or_404
from .models import BlogPost, BlogComment
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
from .forms import BlogPostForm, CommentForm





# trying out multiple objects inside one class-based listView template
class BlogIndexView(ListView):
    context_object_name = 'posts'    
    template_name = 'blog/blog_home.html'
    queryset = BlogPost.objects.all()
    ordering = ['-date_posted']			# filter for newest post first
    paginate_by = 10					# number of posts to show per page

    # already worked on screening-out the tags but the actual filter on home.html has not yet been implemented
    # might switch to a separate DetailView for each context filter, instead
    def get_context_data(self, **kwargs):
        context = super(BlogIndexView, self).get_context_data(**kwargs)
        context['entertainment'] = BlogPost.objects.filter(tag="Entertainment").order_by('-date_posted')
        context['help'] = BlogPost.objects.filter(tag="Help!").order_by('-date_posted')
        context['hobby'] = BlogPost.objects.filter(tag="Hobby").order_by('-date_posted')
        context['jokes'] = BlogPost.objects.filter(tag="Jokes").order_by('-date_posted')
        context['school'] = BlogPost.objects.filter(tag="School").order_by('-date_posted')
        context['social'] = BlogPost.objects.filter(tag="Social").order_by('-date_posted')
        context['tech'] = BlogPost.objects.filter(tag="Tech").order_by('-date_posted')
        # and so on for more models

        return context

##########################################
# this func-based view may also work, just define/add filters to context since it's a dictionary
# def blog_view(request):
# 	context = {'posts': BlogPost.objects.all(),
# 				#'define_more': here }
# 	return render(request, 'blog/blog_base.html')


# this was the original class-based view for home.html (from tutorial)

# class PostListView(ListView):			# quite complicated way of creating views / did not follow the naming convention
# 	model = BlogPost 						# by default, django will look for a template <app>/<model>_<viewtype>.html
# 											# that will be "blog/post_list.html"
	
# 	template_name = 'blog/blog_home.html'
# 	context_object_name = 'posts'		# getting the 'posts' key from "context = {'posts': Post.objects.all(),}"
# 	ordering = ['-date_posted']			# filter for newest post first
# 	paginate_by = 5					# # of posts to show per page
##########################################

class UserPostListView(ListView):
	model = BlogPost 			
	template_name = 'blog/blog_userposts.html'
	context_object_name = 'posts'		# getting the 'posts' key from "context = {'posts': Post.objects.all(),}"
	ordering = ['-date_posted']
	paginate_by = 5	

	def get_queryset(self):		# this defines the filter for the specific user's posts
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return BlogPost.objects.filter(author=user).order_by('-date_posted')



# from .forms import CommentForm
class PostDetailView(LoginRequiredMixin, DetailView):
	model = BlogPost
	template_name = 'blog/blog_postdetail.html'
	post = BlogPost.objects.all()
	context = {'posts': BlogPost.objects.all(),
				'comments': BlogComment.objects.filter(post=post).order_by('-id')} # this line seems not working / wrong


#from .forms import BlogPostForm
class PostCreateView(LoginRequiredMixin, CreateView):		
	model = BlogPost
	form_class = BlogPostForm
	template_name = 'blog/blog_postform.html'
	# fields = ['title', 'content']		# fields for the model // not needed for there is a form_class
	success_url = '/home'

	def form_valid(self, form):			#to automatically get the id of the current logged-in user as the author
		form.instance.author = self.request.user 	#set the author to the current logged-in user
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = BlogPost 
	form_class = BlogPostForm
	template_name = 'blog/blog_postform.html' # note that this template is the same as for the createview
	success_url = '/home/'

	def form_valid(self, form):			
		form.instance.author = self.request.user 	#to automatically get the id of the current logged-in user as the author
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()

		if self.request.user == post.author:
			return True
		return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):		
	model = BlogPost
	template_name = 'blog/blog_postconfirmdelete.html'
	success_url = '/home/'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()

		if self.request.user == post.author:
			return True
		return False		



#####################################################
# find a way to render another website (youtube) inside this specific view // embed website
# will act as a browser inside the website
# def exp(request):
# 	return render(request, 'blog/experiment_page.html', {'title': 'Experiments'})
	
def exp(request):
	return render(request, 'blog/blog_exp.html', {'title': 'Experiment Page'})

# experiment ng comment section







