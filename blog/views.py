from django.shortcuts import render

# Create your views here.
def allblog_view(request):
	ctx = {}
	return render(request, 'blog.html', ctx)