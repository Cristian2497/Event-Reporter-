from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def homepage_view(request):
    return render(request, 'index.html', )


