import uuid
from unittest.util import _MAX_LENGTH

from services.aiding_functions import department_finder
from .choices import *
from django.db import models
from autoslug import AutoSlugField
from tinymce.models import HTMLField
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class Department(models.Model):
    department_name = models.CharField(max_length = 100)
    department_id = models.CharField(max_length = 100)
    department_school = models.CharField(max_length = 100,choices = SCHOOL_CHOICES)
    def __str__(self):
        return self.department_name
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = PhoneNumberField(blank = True)
    role = models.CharField(max_length = 100,choices = ROLE_CHOICES,blank = True, null=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE,null = True)
    admitted_year = models.CharField(max_length = 500,null=True)
    slug = models.SlugField(blank=True)
    def __str__(self):
        return self.user.username
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = uuid.uuid4()
        super(Profile, self).save(*args,**kwargs)

    
class Query(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    date_of_creation = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length = 200,choices = STATUS_CHOICES)
    description = HTMLField()
    department = models.ForeignKey(Department,on_delete = models.CASCADE)
    admitted_year = models.CharField(max_length = 200)
    type = models.CharField(max_length = 100)
    slug = AutoSlugField(populate_from = "title",unique=True,blank = True,editable = True)
    def __str__(self):
        return self.title
@receiver(post_save,sender = User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user = instance,role = "Unauthorized",department = None)
        instance.profile.save()
@receiver(post_save, sender = User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()