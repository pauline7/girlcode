from listings.models import *
from django.contrib.auth.models import User
from django import forms
from django.forms import Textarea, fields     ### 
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

# class PackageForm(forms.ModelForm):
#     class Meta:
#         model = Package
#         fields = ['title', 'date', 'agency', 'location', 'price', 'images', 'description', 'category']
#         widgets = {
#             'description': Textarea(attrs={
#                 'cols': 80,
#                 'rows': 4,
#                 'class': 'form-control'
#             }),
#         }

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        #self.helper.form_action = reverse_lazy('index')

    class Meta:  
        # To specify the model to be used to create form  
        model = Post 
        # It includes all the fields of model  
        fields = ['title', 'images', 'description'] 
        # widgets = {
        #     'date': forms.DateInput(attrs={
        #         'type': 'date',
        #     }),
        # }

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ['content']
        widgets = {
          'content': Textarea(attrs={'rows':2, 'cols':40}),
        }