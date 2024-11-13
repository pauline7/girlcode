from django import template #for group permissions
from django.contrib.auth.models import Group  #for group permissions

# For group permissions
register = template.Library() 

@register.filter(name='has_group') 
def has_group(user, group_name):
    group =  Group.objects.get(name=group_name) 
    return group in user.groups.all() 
