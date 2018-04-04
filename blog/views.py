from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	template_name='blog/post_list.html'
	return render (request,template_name)