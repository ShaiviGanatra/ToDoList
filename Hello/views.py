from django.shortcuts import render, redirect, HttpResponse
from .models import TodoList
# Create your views here.

def index(request):

    list = TodoList.objects.all()
    # dict1 = {'record':list}
    return render(request, 'index.html',{'record':list})

def create(request):
    print(request.POST)
    title = request.GET['title']
    subject = request.GET['subject']
    incharge = request.GET['incharge']
    submission_date = request.GET['submission_date']
    list_details = TodoList(title=title,subject=subject,incharge=incharge,submission_date=submission_date)
    list_details.save()
    return redirect('/')

def add_new(request):
    return render(request, 'add_new.html')

def delete(request , id):
    list = TodoList.objects.get(pk=id)
    list.delete()
    return redirect('/')

def edit(request , id):
    list = TodoList.objects.get(pk=id)
    return render(request, 'edit.html',{'record':list})

def update(request , id):
    list = TodoList.objects.get(pk=id)
    list.title = request.GET['title']
    list.subject = request.GET['subject']
    list.incharge = request.GET['incharge']
    list.submission_date = request.GET['submission_date']
    list.save()
    return redirect('/')
