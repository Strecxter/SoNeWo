from django import forms
from django.forms import ModelForm, Textarea
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'text', 'detailed_text')
		widgets = {
            'title': Textarea(attrs={'cols': 80, 'rows': 1}),
			'text': Textarea(attrs={'cols': 80, 'rows': 4}),
			'detailed_text': Textarea(attrs={'cols': 80, 'rows': 8}),
        }