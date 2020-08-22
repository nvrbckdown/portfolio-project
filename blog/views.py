from django.shortcuts import render
from .models import Blog

# Create your views here.
def allblog_view(request):
	blogs = Blog.objects.all()
	ctx = {
		"blogs": blogs
	}
	return render(request, 'blog/blog.html', ctx)