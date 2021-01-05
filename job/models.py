from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from cities_light.models import Region
# Create your models here.
job_type_choices = [
    ('Full-time','Full-time'),
    ('Part-time','Part-time'),
]
class Categories(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Job(models.Model):
    owner = models.ForeignKey(User,related_name='job_owner',on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=256)
    job_type = models.CharField(max_length=256,choices=job_type_choices,default='Full-time')
    location = models.ForeignKey(Region,related_name='location',on_delete=models.CASCADE,null=True)
    description = models.TextField(max_length=2500,null=True)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.PositiveIntegerField(default=1)
    salary = models.PositiveIntegerField(default=1)
    experience = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Categories,related_name='jobs',on_delete=models.CASCADE,null=True)
    slug = models.SlugField(null=True,blank=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)


    def __str__(self):
        return self.title


class Apply(models.Model):
    job = models.ForeignKey(Job,related_name='apply_job',on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100,null=True)
    website = models.URLField(null=True,blank=True)
    cv = models.FileField(upload_to='apply/',null=True)
    cover_letter = models.TextField(max_length=500,null=True)
    created_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
