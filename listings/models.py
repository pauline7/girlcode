from django.db import models
from django.urls import reverse 
from django.db.models import UniqueConstraint # Constrains fields to unique values
from django.db.models.functions import Lower # Returns lower cased value of field
import uuid # Required for unique packages instances
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.contrib.auth.models import User


class PostInstance(models.Model):

    """Model representing a specific package)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular package")
    post= models.ForeignKey('Post', on_delete=models.RESTRICT, null=True)
    # imprint = models.CharField(max_length=200)
    post_date = models.DateField(null=True, blank=True)


    class Meta:
        ordering = ['post_date']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.post.title})'

class Post(models.Model):
    """Model representing a package."""
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4,
    #                       help_text="Unique ID for this particular package")
    title = models.CharField(max_length=200)
    created = models.DateField(auto_now=True)
    images = models.ImageField(upload_to='listings/media/static/post_images', blank='True')
    description = models.TextField( max_length=10000, help_text="Whats your Story?", blank='False')


    class Meta:
        ordering = ['-created']


    # display_category.short_description = 'Category'

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.title})'

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('post-detail', args=[str(self.id)])



class PostComment(models.Model):
    post_connected = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField( max_length=300, help_text="Add a comment...")
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.author) + ', ' + self.post_connected.title[:40]