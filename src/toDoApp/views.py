from django.shortcuts import render
from .models import Task, CompletedTask

# Create your views here.

def home_page(request):
    return render(request, "toDoApp/home_page.html")

def view_task(request):
    task = Task.objects.all()
    # context is a tuple array/dictionary that you pass to the HTML
    # makes the HTML more "dynamic"
    context = {
        "task_list": task,
    }
    return render(request, "toDoApp/view_task.html", context)

def view_past(request):
    complete_task = CompletedTask.objects.all()
    context = {
        "complete_task_list": complete_task,
    }
    return render(request, "toDoApp/view_past.html", context)