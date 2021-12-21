from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from tablib import Dataset
import joblib
import pandas as pd


def home(request):
    return  render(request,"home.html")
def result(request):
#Code lan1
    cls=joblib.load('finalized_model.sav')
    lis=[]
    lis.append(request.GET['w7'])
    lis.append(request.GET['w5'])
    lis.append(request.GET['w3'])
    lis.append(request.GET['hnk2'])
    lis.append(request.GET['hnk1'])
    lis.append(request.GET['hnk'])
    lis.append(request.GET['htk2'])
    lis.append(request.GET['htk1'])
    lis.append(request.GET['htk'])

    sumation=cls.predict([lis])
    return render(request,"result.html",{'something':True,'sum':sumation})
 