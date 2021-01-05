from django.db import models

# Create your models here.
class ContactInfo(models.Model):
    name = models.CharField(max_length=50,null=True)
    place = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name
