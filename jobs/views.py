from django.shortcuts import render
from .models import Job

def home_view(request):
	jobs = Job.objects.all()
	print(jobs)
	ctx = {
		"jobs": jobs
	}
	return render(request, 'jobs/home.html', ctx)