from django.shortcuts import render
from .models import Wpis
from .forms import WpisFormularz
from django import db
from . import ngramy1
from django.utils import timezone
# Create your views here.
def home(request):
    wpisy = Wpis.objects.all()
    return render(request,'home.html', {'wpisy': wpisy})
def generate(request):
    forma = WpisFormularz()
    return render(request,'generate.html', {'form': forma})
def generateend(request):
    formularz = WpisFormularz(request.POST)
    if(formularz.is_valid()):
        start_phrase = formularz.cleaned_data['start']
        gram = formularz.cleaned_data['gram']
        if gram == 1:
            tekst = " ".join(ngramy1.unigram())
            if len(tekst.split(' '))<10:
                return render(request, 'generateend.html', {'message': "Generated ngram is too short! Try again!", 'type': "error"})
            title = tekst.split('.')[0]+'.'
            Wpis.objects.create(tytul=title,
                                tresc=tekst,
                                gram=gram,
                                data=timezone.now())
            return render(request, 'generateend.html', {'message': "Generated successfully!", 'type': "ok"})
        elif gram == 2:
            tekst = " ".join(ngramy1.bigram(start_phrase))
            if len(tekst.split(' '))<10:
                return render(request, 'generateend.html', {'message': "Generated ngram is too short! Try again!", 'type': "error"})
            title = tekst.split('.')[0]+'.'
            Wpis.objects.create(tytul=title,
                                tresc=tekst,
                                gram=gram,
                                data=timezone.now())
            return render(request, 'generateend.html', {'message': "Generated successfully!", 'type': "ok"})
        elif gram == 3:
            tekst = " ".join(ngramy1.gram3(start_phrase))
            if len(tekst.split(' '))<10:
                return render(request, 'generateend.html', {'message': "Generated ngram is too short! Try again!", 'type': "error"})
            title = tekst.split('.')[0]+'.'
            Wpis.objects.create(tytul=title,
                                tresc=tekst,
                                gram=gram,
                                data=timezone.now())
            return render(request, 'generateend.html', {'message': "Generated successfully!", 'type': "ok"})
        elif gram == 4:
            tekst = " ".join(ngramy1.gram4(start_phrase))
            if len(tekst.split(' '))<10:
                return render(request, 'generateend.html', {'message': "Generated ngram is too short! Try again!", 'type': "error"})
            title = tekst.split('.')[0]+'.'
            Wpis.objects.create(tytul=title,
                                tresc=tekst,
                                gram=gram,
                                data=timezone.now())
            return render(request, 'generateend.html', {'message': "Generated successfully!", 'type': "ok"})
        else:
            return render(request, 'generateend.html', {'message': "I cannot generate that ngram!", 'type': "error"})
    else:
        return render(request, 'generateend.html', {'message': "FORM error!", 'type': "error"})