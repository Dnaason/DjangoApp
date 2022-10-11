from urllib import response
import africastalking
from distutils.command.clean import clean
import email
from http import client
from django.shortcuts import HttpResponse, render
from .models import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

username = "dnaason11@gmail.com"
api_key = "c5595115784319953a019773f0ebbf7cd78a6ecc5c1d2f7932b72c9c0783f9a3"
africastalking.initialize(username,api_key)

# Create your views here.
def index(request):
    selectdata = Clients.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']
        insertdata = Clients(name=name, email=email, password=password, repassword=repassword)
        try:
            insertdata.save()
            return render(request, 'index.html',{'message':'data sent successfull'}, {'data':selectdata})
        except:
            return render(request, 'index.html',{'message':'data sent failed'} )
    return render(request, 'index.html',{'data':selectdata})
def resigister(request):
    return render(request, 'register.html')

def delete(request):
    delete = Clients.objects.filter(id=id).delete()
    return render(request, 'index.html',{'data':delete})

@csrf_exempt
def idaussd(request):
    if request.method == 'POST':
        session_id = request.POST.get("sessionId", None)
        serviceCode = request.POST.get("serviceCode", None)
        phone_number = request.POST.get("phoneNumber", None)
        text  = request.POST.get("text")
        response = ""
        if text == '':
            response  = "CON What would you want to check \n"
            response += "1. My Account \n"
            response += "2. My phone number"

        elif text == '1':
        # Business logic for first level response
            response  = "CON Choose account information you want to view \n"
            response += "1. Account number"

        elif text == '2':
        # This is a terminal request. Note how we start the response with END
            response = "END Your phone number is " + phone_number

        elif text == '1*1':
        # This is a second level response where the user selected 1 in the first instance
            accountNumber  = "ACC1001"
        # This is a terminal request. Note how we start the response with END
            response = "END Your account number is " + accountNumber
        else :
            response = "END Invalid choice"
    return HttpResponse(response)