from django.shortcuts import render , get_object_or_404
from .models import Blog

def home(request):
    blog = Blog.objects.all() 
    return render(request, 'home.html', {'blog':blog})

def detail(request, id):
	blog = get_object_or_404(Blog, pk = id)
	return render(request, 'detail.html', {'blog':blog})