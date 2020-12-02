from django import forms
from django.db import models
from .models import LoungeUnsentLetters


class ULForm(forms.ModelForm):
	message = forms.CharField(widget=forms.Textarea())

	class Meta:
		model = LoungeUnsentLetters
		fields = ["title", "letter_for", "message", "attach_file",]
