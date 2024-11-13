from django.contrib import admin
from django import forms
#from phonenumber_field.widgets import PhoneNumberPrefixWidget


# class AgencyForm(forms.ModelForm):
#     class Meta:
#         widgets = {                          
#             'phone': PhoneNumberPrefixWidget(initial='US'),
#         }


# Register your models here.
from .models import Post, PostInstance

#admin.site.register(Package)
#admin.site.register(Agency)
#admin.site.register(Category)
admin.site.register(PostInstance)

# Define the admin class
# class AgencyAdmin(admin.ModelAdmin):
#     # form = AgencyForm
#     list_display = ('agency_name', 'agency_email', 'created', 'verified_agency')
#     fields = ('agency_name', 'agency_email', 'agency_description', 'logo', 'phone')

# Register the admin class with the associated model
#admin.site.register(Agency, AgencyAdmin)

# Register the Admin classes for Book using the decorator
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    #list_filter = ('title', 'created')
    list_display = ('title', 'created', 'id')
    fields = ('title', 'images', 'description')

# Register the Admin classes for BookInstance using the decorator
# @admin.register(PostInstance)
# class PostInstanceAdmin(admin.ModelAdmin):
#     list_filter = ('post', 'created')