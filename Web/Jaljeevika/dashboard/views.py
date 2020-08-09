from django.shortcuts import render,redirect
from .models import fpoproduct,FPO
# Create your views here.
from .forms import (
    ProductForm
)

	
def marketview(request):

	products = fpoproduct.objects.all().order_by('-created')
	
	return render(request,'marketview.html',{'products':products})

def home(request):
	return render(request,'home.html')

def fpodashboard(request):
	fpos=FPO.objects.all()
	if request.method=='POST':
		searchVal=request.POST.get('search')
		category=request.POST.get('categoryVal')
		print(searchVal)
		fpos=FPO.objects.filter(statename__exact=searchVal)
	return render(request,'fpodashboard.html',{'fpos':fpos})


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

def forminput(request):
	if request.method == 'POST':
		form = ProductForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect(reverse('about'))
	

	else:
		form = ProductForm()
		args = {'form': form}
		return render(request, 'forminput.html', args)


