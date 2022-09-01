import email
from django.shortcuts import render
from django.http import HttpResponse

from rest_api_app.models import Members
# Create your views here.

def index(request):
    SignUpMembers = Members.objects.all().values()
    return HttpResponse(SignUpMembers)

# def index1(request):
#     return HttpResponse("HELLO WORLD !!! ABDUL HASEEB IMRAN")

def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  z = request.POST['email']
  Members = addrecord(firstname=x, lastname=y, email=z)
  Members.save()
  return HttpResponse(Members)