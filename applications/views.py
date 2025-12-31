from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Application
from jobs.models import Job

@login_required
def apply_job(request, job_id):
    job = Job.objects.get(id=job_id)

    if request.method == 'POST':
        resume = request.FILES['resume']
        Application.objects.create(
            user=request.user,
            job=job,
            resume=resume
        )
        return redirect('job_list')

    return render(request, 'applications/apply.html', {'job': job})

@login_required
def my_applications(request):
    applications = Application.objects.filter(user=request.user)
    return render(request, 'applications/my_applications.html', {
        'applications': applications
    })
