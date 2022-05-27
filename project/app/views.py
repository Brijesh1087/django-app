from django.shortcuts import render

# Create your views here.
def index(request): #home
	return render(request,'app/index.html')

def join(request): #join
	return render(request,'app/join.html')

def about(request): #about
	return render(request,'app/about.html')

def contact(request): #contact
	return render(request,'app/contact.html')