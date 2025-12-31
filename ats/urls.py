from django.contrib import admin
from django.urls import path
from jobs.views import job_list
from applications.views import apply_job , my_applications

urlpatterns = [
    path('my-applications/', my_applications, name='my_applications'),
    path('admin/', admin.site.urls),
    path('', job_list, name='job_list'),
    path('apply/<int:job_id>/', apply_job, name='apply_job'),
]
