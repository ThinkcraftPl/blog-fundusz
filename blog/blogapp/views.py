from django.shortcuts import render
from .models import Wpis
from .forms import WpisFormularz
from django import db
# Create your views here.
def home(request):
    wpisy = Wpis.objects.all()
    return render(request,'blogapp/home.html', {'wpisy': wpisy})