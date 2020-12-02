from django.shortcuts import render

# Create your views here.

def utilities_view(request):
	return render(request, 'utilities/post_editor.html')