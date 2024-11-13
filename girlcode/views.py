from django.http import HttpResponse
from django.views.decorators.http import require_GET
from django.shortcuts import render

import json

def privacy(request):
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'terms_and_conditions/privacy.html')

def appads(request):
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'app-ads.txt')

def adsenseads(request):
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'ads.txt')

@require_GET
def digital_assets(request):
    #return HttpResponse(content_type='application/json')
    data_file = open('./static/.well-known/assetlinks.json') 
    return HttpResponse(data_file, content_type='application/json')