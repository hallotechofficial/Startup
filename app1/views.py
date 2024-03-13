from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseForbidden
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from startup.settings import EMAIL_HOST_USER
from smtplib import SMTPConnectError
from .models import Post
from .forms import PostForm


def home(request): 
    return render(request,'index.html')

def about(request): 
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        
        email_body = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"

       
        msg = EmailMultiAlternatives(
            subject=subject,
            body=email_body,
            from_email=email,
            to=['hallotechofficial@gmail.com']
        )
        msg.send()
    return render(request,'about.html')

def contact(request): 
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        email_body = f"Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"

        msg = EmailMultiAlternatives(
            subject=subject,
            body=email_body,
            from_email=email,
            to=['hallotechofficial@gmail.com']
        )
        msg.send()

    return render(request, 'contact.html')


def service(request): 
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        service = request.POST.get('service')
        message = request.POST.get('message')
        
        email_body = f"Name: {name}\nEmail: {email}\nService: {service}\nMessage: {message}"

        msg = EmailMultiAlternatives(
            subject='Service Request',  # Set the subject here
            body=email_body,
            from_email=email,
            to=['hallotechofficial@gmail.com']
        )

        msg.send()

    return render(request, 'service.html')

def project(request):
    Posts = Post.objects.all()
    return render(request, 'projects.html', {'Posts': Posts})