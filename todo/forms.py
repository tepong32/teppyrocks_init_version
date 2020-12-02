from django import forms
from django.db import models
from .models import ToDoList, ToDoItems


class ToDoForm(forms.ModelForm):
	desc = forms.CharField(widget=forms.Textarea())

	class Meta:
		model = ToDoList
		fields = ["category", "desc", "finish_by"]


# not making any sense // not being used atm
class ToDoItemsForm(forms.ModelForm):
	desc = forms.CharField(widget=forms.Textarea())

	class Meta:
		model = ToDoList
		fields = ["category", "desc", "finish_by"]
