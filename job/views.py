from django.shortcuts import render
from . models import Job


def job_list (requset):
    job_lists = Job.objects.all()
    context = { 'jobs' : job_lists}
    return render (requset , 'job/job_list.html' , context)


def job_details (requset , id):
    job_lists = Job.objects.get(id = id )
    context = { 'job_details' : job_lists}
    return render (requset , 'job/job_detalis.html' , context)