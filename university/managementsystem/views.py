from django.shortcuts import render, HttpResponse, redirect
from .forms import BlogForm, SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django import forms
from .models import Blogs, Profile

# Create your views here.
def view_blogs(request):
    content=Blogs.objects.all().values_list('id', 'title')
    return  render(request, 'view_blogs.html',{
        'content': content,
    })
def welcome(request):
    return redirect('login')

def home(request):
    return render(request, 'home.html',)

def add_blog(request):
    if request.method=='GET':
        form=BlogForm
        return render(request, 'add_blogs.html', {
            'form': form,
        })
    if request.method=='POST':
        form=BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("saved!!!!!!!!!!!!!")
        else:
            return HttpResponse("form is invalid")

def signup(request):


    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            userObj=form.cleaned_data
            username=userObj['username']
            password=userObj['password1']
            if not(User.objects.filter(username=username).exists()):
                user=form.save()
                user.refresh_from_db()
                pr=Profile()
                pr.user=username
                pr.age=form.cleaned_data.get('age')
                pr.profile=form.cleaned_data.get('profile')
                pr.branch=form.cleaned_data.get('branch')
                pr.contact_info = form.cleaned_data.get('contact_info')
                pr.reg_no = form.cleaned_data.get('reg_no')
                pr.email_id = form.cleaned_data.get('email_id')
                pr.address = form.cleaned_data.get('address')
                pr.current_sem = form.cleaned_data.get('current_sem')
                pr.save()
                user.save()
                user=authenticate(username=username, password=password)
                login(request, user)
                return redirect('home')

            else:
                raise forms.ValidationError('look like username with this username or password already exist')

    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form,})



