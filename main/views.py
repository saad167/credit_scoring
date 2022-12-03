from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse




def index(request):

    context = {"name":"saad"} 

    return render(request, 'index.html',context = context)


def add(request):

    val1 = int(request.GET["num1"])
    val2 = int(request.GET["num2"])

    res = val1 + val2 

    return render(request,"result.html",{"result":res})