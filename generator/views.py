from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, 'html_files/first.html')


def password(request):

    chars=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        chars.extend(list('0123456789'))
    if request.GET.get('special'):
        chars.extend(list('~`!@#$%^&*()_'))
    len=int(request.GET.get('length',10))
    thepassword=""
    for i in range(len):
        thepassword=thepassword+random.choice(chars)

    return render(request,  'html_files/password.html',{'Pass':thepassword})

    

    