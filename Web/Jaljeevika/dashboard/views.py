from django.shortcuts import render
from .models import fpoproduct
# Create your views here.


	
def marketview(request):
	products = fpoproduct.objects.all().order_by('-created')
	#,{'products':products}
	return render(request,'marketview.html')

def home(request):
	return render(request,'home.html')

def fpodashboard(request):
	return render(request,'fpodashboard.html')


def knowledge(request):
	return render(request,'knowledge.html')

def contact(request):
	return render(request,'contact.html')


def forum(request):
	return render(request,'forum.html')


def about(request):
	return render(request,'about.html')


def gallery(request):
	return render(request,'gallery.html')

def knowledge(request):
	return render(request,'knowledge.html')




