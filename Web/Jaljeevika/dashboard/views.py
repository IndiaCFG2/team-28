from django.shortcuts import render

# Create your views here.
def render_marketview(request):
	return render(request,'base.html')
	
def render_fpodashboard(request):
	return render(request,'fpodashboard.html')

def render_forum(request):
	return render(request,'forum.html')

def render_marketplace(request):
	return render(request,'marketplace.html')

