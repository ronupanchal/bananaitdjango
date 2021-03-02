from django.shortcuts import render
from .models import TblContact, TblSlider, TblTeam


# Create your views here.
def index(request):       
    contacts = TblContact.objects.all()
    sliders = TblSlider.objects.all()
    print(contacts)
    return render(request, 'index.html', {'contacts': contacts, 'sliders': sliders})

def ourteam(request):
    teams = TblTeam.objects.all()
    return render(request, 'ourteam.html', {'teams': teams})