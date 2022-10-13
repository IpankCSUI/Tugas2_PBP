from http.client import HTTPResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.urls import reverse
from todolist.form import CreateTask
from todolist.models import Task
from django.core import serializers

# Create your views here.
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    task_list = Task.objects.filter(user = request.user).all()
    context = {
        'task_list': task_list
    }
    return render(request, 'todolist.html', context)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("todolist:show_todolist")
    context = {}
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

@login_required(login_url='/todolist/login/')
def create_task(request):
    form = CreateTask()
    if request.method == 'POST':
        form = CreateTask(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('todolist:show_todolist')
    else:
        form = CreateTask(initial={'user': request.user})
    context = {'form': form}
    return render(request, 'create_task.html', context)

@login_required(login_url="/todolist/login")
def show_todolist_json(request):
    tasks = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', tasks), content_type='application/json')

def add_task(request):
    if request.method == "POST":
        judul = request.POST.get('title')
        deskripsi = request.POST.get('description')
        new_task = Task(user=request.user, title=judul, description=deskripsi, date=datetime.now())
        new_task.save()
    return HttpResponse('')