from django.shortcuts import render
from .models import Doctor
# Create your views here.
def NewProject(request):

    docs=Doctor.objects.all()
    
    return render(request,"NewProject.html", {'docs': docs})