from django.shortcuts import render
from .models import Parties_result

# Create your views here.

def index(request):
    return render(request, 'index.html')


def result(request):
    results = Parties_result.objects.all()

    return render(request, 'result.html', {'results':results})

def polling_unit(request):

    return(render(request, 'polling_unit.html'))