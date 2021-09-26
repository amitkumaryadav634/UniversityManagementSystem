from django import forms
from .models import Blogs
from django.contrib.auth.forms import UserCreationForm

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blogs
        exclude=()

class SignUpForm(UserCreationForm):
    PROFILE_CHOICES=(
        ('Professor', 'Professor'),
        ('Student', 'student'),
    )
    BRANCH_CHOICES=(
        ('CSE', 'CSE'),
        ('IT', 'IT'),
        ('ENTC', 'ENTC'),
        ('MECH', 'MECH'),
    )
    age = forms.IntegerField()
    profile = forms.CharField()
    branch = forms.CharField()
    contact_info = forms.CharField()
    reg_no = forms.CharField()
    email_id = forms.EmailField()
    address = forms.CharField()
    current_sem = forms.CharField()