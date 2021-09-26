from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blogs(models.Model):
    title=models.CharField(max_length=32, default='')
    blog=models.TextField()
    username=models.CharField(max_length=32)
    date_of_submission=models.DateField(auto_now=True)

class Profile(models.Model):
    PROFILE_CHOICES = (
        ('Professor', 'Professor'),
        ('Student', 'student'),
    )
    BRANCH_CHOICES = (
        ('CSE', 'CSE'),
        ('IT', 'IT'),
        ('ENTC', 'ENTC'),
        ('MECH', 'MECH'),
    )
    user=models.CharField(max_length=64, blank=True)
    age=models.IntegerField(blank=True)
    profile=models.CharField(max_length=32, blank=True, choices=PROFILE_CHOICES)
    branch=models.CharField(max_length=32, blank=True, choices=BRANCH_CHOICES)
    contact_info=models.CharField(max_length=32, blank=True)
    reg_no=models.CharField(max_length=10, blank=True)
    email_id=models.EmailField(max_length=20, blank=True)
    address=models.TextField(blank=True)
    current_sem=models.CharField(max_length=12, blank=True)