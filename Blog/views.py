from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.decorators import login_required
import datetime
# Create your views here.
p = '2018-12-24Introduction'
def home(request):
	obj = Post.objects.get(PriKey=p)
	return render(request,'MyBlog.html',{'obj':obj})

def about(request):
	return render(request,'About.html',{})

@login_required
def post(request):
	if request.method=='POST':
		obj = Post()
		obj.Heading = request.POST['Heading']
		obj.Content = request.POST['Content']
		obj.PriKey = str(datetime.date.today())+obj.Heading
		obj.save()
		return redirect('/Blog/home/')
	return render(request,'post.html',{})

def explore(request):
	obj = Post.objects.all()
	return render(request,'explore.html',{'obj':obj})

def goto(request,key):
	obj = Post.objects.get(PriKey=key)
	return render(request,'MyBlog.html',{'obj':obj})

