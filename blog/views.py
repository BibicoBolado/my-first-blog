from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.utils import timezone

# Create your views here.

from .models import Post

def home(request):
	posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('created_date')
	template_name='blog/post_list.html'
	context={}
	context['posts']=posts
	return render (request,template_name,context)

def post(request,slug):
	post=get_object_or_404(Post,slug=slug)
	template_name='blog/postagem.html'
	context={}
	context['post']=post
	return render (request,template_name,context)
