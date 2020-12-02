from django import forms
from pagedown.widgets import PagedownWidget
from .models import BlogPost, BlogComment


class BlogPostForm(forms.ModelForm):
    title = forms.CharField(max_length=100)		# i think this can be removed since the same field is in the model
    content = forms.CharField(widget=PagedownWidget())

    class Meta:
    	model = BlogPost
    	fields = ['title', 'tag', 'content']




from bootstrap_modal_forms.forms import BSModalForm

class ModalPostForm(BSModalForm):
	class Meta:
		model = BlogPost
		fields = ['title', 'content', 'tag']



class CommentForm(forms.ModelForm):
	class Meta:
		model = BlogComment
		fields = ('content',)