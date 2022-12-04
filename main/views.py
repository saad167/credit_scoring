from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import numpy as np

import joblib




def index(request):

    context = {"name":"saad"} 

    return render(request, 'index.html',context = context)


def predict(request):
    
    classifier = joblib.load('main\saved_model.sav')

    liste = []

    liste.append(int(request.GET["age"]))
    liste.append(int(request.GET["education_level"]))
    liste.append(int(request.GET["employ"]))
    liste.append(int(request.GET["income"]))
    data_array = np.asarray(liste)

    arr = data_array.reshape(1,-1)
    answer = classifier.predict(arr)
    if(answer == 1):
      finalanswer='we can not give loan to the customer'
    elif(answer == 0):
      finalanswer = 'we can give loan to the customer'


    return render(request,"result.html",{"result":finalanswer})