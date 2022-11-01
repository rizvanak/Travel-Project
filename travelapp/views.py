from django.http import HttpResponse
from django.shortcuts import render
from .models import place, date


# Create your views here.
def fun(request):
    obj=place.objects.all()

    return render(request,"index.html",{'results':obj})

# def fun1(request):
#     obj1=date.objects.all()
#     return render(request,"index.html",{'blogs':obj1})

def fun1(request):
    obj=date()
    obj.day=2
    obj.month="jan"
    obj.desc="abcdefghijklmnopqrstuvwxyz"
    return render(request,"index.html",{'blog':obj})
def addition(request):
    num1=int(request.POST["num1"])
    num2=int(request.POST["num2"])
    num3=num1+num2
    return render(request,"result.html",{"add":num3})
