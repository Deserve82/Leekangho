from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    blog = Post.objects
    return render(request, 'home.html',{'blog':blog})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Post, pk=blog_id)
    return render(request, 'detail.html',{'blog_detail':blog_detail})
# Create your views here.
