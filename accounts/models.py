from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from cities_light.models import Region
from job.models import Job
# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,related_name='profile_user')
    city = models.ForeignKey(Region,related_name='user_city',on_delete=models.CASCADE,null=True)
    phone_number = models.IntegerField(null=True)
    image = models.ImageField(upload_to='profile/',blank=True)


    def save(self,*args,**kwargs):
        self.slug = slugify(self.user)
        super().save(*args,**kwargs)


    def __str__(self):
        return str(self.user)



@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
