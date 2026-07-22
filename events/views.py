from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Event
from django.contrib.auth.decorators import login_required
from .forms import EventForm
# Create your views here.
def signup_view(req):
    if req.method=="POST":
        form=UserCreationForm(req.POST)
        if form.is_valid():
            user=form.save()
            login(req,user)
            return redirect('dashboard')
    else:
        form=UserCreationForm()
    return render(req,'register.html',{'form':form})
def login_view(req):
    if req.method=="POST":
        form=AuthenticationForm(req.POST,data=req.POST)
        if form.is_valid():
            user=form.get_user()
            login(req,user)
            return redirect('login')
    else:
        form=AuthenticationForm()
    return render(req,'login.html',{'form':form})
def logout_view(req):
    logout(req)
    return redirect('login')
@login_required
def dashboard(req):
    return render(req,'dashboard.html')
def home(req):
    return render(req,'home.html')
def add_event(req):
    if req.method=="POST":
        form=EventForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form=EventForm()
    return render(req,'add_event.html',{'form':form})
def view_event(req):
    data=Event.objects.all()
    return render(req,'view_event.html',{'data':data})
def edit_event(req,id):
    d=get_object_or_404(Event,id=id)
    if req.method=="POST":
        form=EventForm(req.POST,instance=d)
        if form.is_valid():
            form.save()
            return redirect('view_event')
    else:
        form=EventForm(instance=d)
    return render(req,'edit_event.html',{'form':form})
def delete_event(req,id):
    d=get_object_or_404(Event,id=id)
    d.delete()
    return redirect('view_event')


