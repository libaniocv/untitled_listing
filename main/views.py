from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.

def index(request):
    context={}
    return render(request,'index.html',context)

def registrar(request):
    registrado=False
    if request.method=='POST':
        user_form=forms.UserForm(data=request.POST)


        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            registrado=True

        else:
            print user_form.errors
    else:
        user_form=forms.UserForm

    context={
        'user_form':user_form,
        'registered':registrado
    }
    return render(request,'registrar.html',context)