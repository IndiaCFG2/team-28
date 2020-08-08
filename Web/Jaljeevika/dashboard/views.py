from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'base.html')

def fpodashboard(request):
	return render(request,'fpodashboard.html')

def forum(request):
	return render(request,'forum.html')

def marketplace(request):
	return render(request,'marketplace.html')

def about(request):
	return render(request,'about.html')

def gallery(request):
	return render(request,'gallery.html')

def knowledge(request):
	return render(request,'knowledge.html')

def knowledgehubpost(request):
	return render(request,'knowledgehubpost.html')
