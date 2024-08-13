from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from app.forms import *

def djforms(request):
    ESTFO=StudentForm() # it is empty student form
    d={'ESTFO':ESTFO}


    if request.method=='POST':
        SFDO=StudentForm(request.POST)

        if SFDO.is_valid():
            print(SFDO)
            return HttpResponse(str(SFDO.cleaned_data))
        else:
            return HttpResponse('invalid data')
        


    return render(request,'djforms.html',d)