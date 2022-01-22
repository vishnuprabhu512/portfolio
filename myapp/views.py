from django.shortcuts import render
from .models import Contact
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.


def index(request):
	return render(request, 'index.html')


def about(request):
	return render(request, 'about.html')


def birthday(request):
	return render(request, 'birthday.html')


def blogs(request):
	return render(request, 'blogs.html')


def calculator(request):
	return render(request, 'calculator.html')


def clock(request):
	return render(request, 'clock.html')


def contact(request):
	if request.method == "POST":
		Contact.objects.create(
            name=request.POST['name'],
            number=request.POST['number'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message']
			)
		
		name=request.POST['name']
		number=request.POST['number']
		email=request.POST['email']
		subject=request.POST['subject']
		message=request.POST['message']
		subject = 'Portfolio Contact Request'
		message = f"Name: "+str(name)+"\nNumber: "+str(number)+"\nEmail: "+str(email)+"\nSubject: "+str(name)+"\nMessage: "+str(name)+"\n"
		email_from = settings.EMAIL_HOST_USER
		recipient_list = ["v8shn7@gmail.com", ]
		send_mail( subject, message, email_from, recipient_list )

		msg = "Contact Saved Successfully"
		return render(request, 'contact.html', {'msg': msg})
	else:
		return render(request, 'contact.html')
	return render(request,'contact.html')

def portfolio(request):
	return render(request,'portfolio.html')

def texteditor(request):
	return render(request,'texteditor.html')

def tictactoe(request):
	return render(request,'tictactoe.html')

def todo(request):
	return render(request,'todo.html')


