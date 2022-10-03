from .choices import *
from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField
from django.contrib.auth.models import User
# Create your models here.
class Query(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    date_of_creation = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length = 200,choices = STATUS_CHOICES)
    description = HTMLField()
    type = models.CharField(max_length = 100)
    slug = AutoSlugField(populate_from = "title",unique=True,blank = True,editable = True)
    def __str__(self):
        self.title