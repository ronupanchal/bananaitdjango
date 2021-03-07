from django.shortcuts import render
from .models import TblContact, TblSlider, TblTeam, TblTestimonial
from googletrans import Translator, constants

# Create your views here.
def index(request):       
    contacts = TblContact.objects.all()
    sliders = TblSlider.objects.all()
    print(contacts)
    return render(request, 'index.html', {'contacts': contacts, 'sliders': sliders})

def ourteam(request):
    teams = TblTeam.objects.all()
    contacts = TblContact.objects.all()    
    return render(request, 'ourteam.html', {'contacts': contacts,'teams': teams})

def translate(request):    
    contacts = TblContact.objects.all()
    output='test'
    # init the Google API translator
    translator = Translator()
    # translate more than a phrase
    sentences = [
        "Hello everyone",
        "How are you ?",
        "Do you speak english ?",
        "Good bye!"
    ]
    translations = translator.translate(sentences, dest="gu")
    for translation in translations:
        print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
    return render(request, 'translation.html', {'contacts': contacts, 'hello': output })

def testimonial(request):    
    contacts = TblContact.objects.all()
    testimonials = TblTestimonial.objects.all()
    return render(request, 'testimonial.html', {'contacts': contacts, 'testimonials': testimonials })    