from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    NAME_MAX_LENGTH = 128
    
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique = True)
    views = models.IntegerField(default=0) # exercise question
    likes = models.IntegerField(default=0) # exercise question
    slug = models.SlugField(unique=True)

    def __str__(self): #for debugging
        return self.name 

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
        if self.views < 0:
            self.views = 0

    class Meta:
        verbose_name_plural = "Categories" # for fixing 'Categorys'

class Page(models.Model):
    TITLE_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self): # for debugging
        return self.title

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    # additional user attributes
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username   

