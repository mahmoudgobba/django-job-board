from django.shortcuts import render
from .models import ContactInfo
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def send_email(request):
    myinfo = ContactInfo.objects.first()
    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']
        print (email)

        send_mail(subject, message,email,['mahmoudgobba51@gmail.com',] ,fail_silently=False,)


    return render(request,'contact/contact.html',{'myinfo':myinfo})
