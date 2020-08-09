from django.shortcuts import render,redirect
from .models import fpoproduct,FPO,ForumComment
import smtplib
from django.http import HttpResponseRedirect
# Create your views here.
from .forms import (
    ProductForm
)
from .templatetags import get_dict


    	
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
	if (request.method)=="POST":
			mailto =request.POST['email']
			name=request.POST['name']
			subject=request.POST['subject']
			msg=request.POST['message']
			mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
			mailServer.starttls()
			gmailaddress='cfgteam28@gmail.com'
			gmailpassword=''
			mailServer.login(gmailaddress , gmailpassword)
			mailServer.sendmail(gmailaddress, mailto , msg)
			mailServer.quit()
			return HttpResponseRedirect(request.path_info)
	else:
		return render(request,'contact-us.html')
	return render(request,'contact-us.html')

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
			print(form)
			form.save()
			return redirect('about')

	else:
		form = ProductForm()
		args = {'form': form}
		return render(request, 'forminput.html', args)


def forum(request):
	fpos=FPO.objects.all()
	form={}
	parents=[]
	if request.method=='POST':
		comments=ForumComment.objects.all()
		replies={}
		for oneCom in comments:            
			print(oneCom)
			if oneCom.parent!=None:
				replies[oneCom.parent.sno].append(oneCom.comment)
			else:
				replies[oneCom.sno]=[]
		parent = request.POST.get("Parentsno")
		comment = request.POST.get('comment')
		username = request.POST.get('username')
		if parent=='None':
			parents.append(parent)
			fpoFid = request.POST.get("chose_fpo")
			fpo=FPO.objects.get(fid=fpoFid)
			comment=ForumComment(comment=comment,user=username,fpo=fpo)
			form={'comment':comment,'username':username,'fpo':fpo}
		else:
			fpId=request.POST.get("fpoNo")
			print(fpId)
			fpo=FPO.objects.get(fid=fpId)
			parentComment=ForumComment.objects.get(sno=parent)
			comment=request.POST.get("reply")
			username=request.POST.get("username")
			comment = ForumComment(comment=comment, user=username, fpo=fpo,parent=parentComment)
		comment.save()
	comments=ForumComment.objects.all()
	print(comments)
	replies={}
	for oneCom in comments:            
		print(oneCom)
		if oneCom.parent!=None:
			replies[oneCom.parent.sno].append(oneCom.comment)
		else:
			replies[oneCom.sno]=[]
	return render(request, 'forum.html',{'fpos':fpos,'comments':comments,'replies':replies,'parents':parents})




