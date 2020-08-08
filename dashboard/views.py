from django.shortcuts import render,redirect
from .models import FPO,ForumComment
# Create your views here.

def forumComment(request):
    fpos=FPO.objects.all()
    l=[]
    l1=[]
    form={}
    for i in fpos:
        l.append(i.name)
        l1.append(i.fid)
    if request.method=='POST':
        comment=request.POST.get('comment')
        username = request.POST.get('username')
        if username=='':
            username='Anonymous'
        fpoFid=request.POST.get("chose_fpo")
        fpo=FPO.objects.get(fid=fpoFid)
        comment=ForumComment(comment=comment,user=username,fpo=fpo)
        comment.save()
        form={'comment':comment,'username':username,'fpo':fpo}
    return render(request, 'dashboard/forum.html',{'fpos':fpos})