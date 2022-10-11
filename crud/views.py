from re import A
from django.shortcuts import render

from .models import Detail

# Create your views here.

def crud(request):
    if request.method == 'POST':
        Fname = request.POST['Fname']
        Lname = request.POST['Lname']
        Age = request.POST['Age']
        Phone = request.POST['Phone']
        insertData = Detail(Fname = Fname, Lname = Lname, Age = Age, Phone = Phone)
        insertData.save()
    return render(request, 'crud.html')
