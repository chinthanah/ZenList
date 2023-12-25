from django.shortcuts import render
from home.models import Task

# Create your views here.
def home(request):
    context={'success':False,'name':'Chinthana'}
    if request.method=="POST":
        title=request.POST['title']
        desc=request.POST['desc']
        print(title,desc)
        ins=Task(Tasktitle=title,Taskdesc=desc)
        ins.save()
        context={'success':True}
    return render(request,'index.html',context)
def tasks(request):
    alltask=Task.objects.all()
    context={'tasks':alltask}
    return render(request,'tasks.html',context)
