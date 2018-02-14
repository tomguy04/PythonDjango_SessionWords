# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
# the index function is called when root is visited
def index(request):
    #return the form.
    return render(request,"session_words/form.html")
def process(request):
    #request.session.modified = True
    houseDict = {}
    request.session['words'] = request.POST['name']
    try:
        request.session['history']
        print "history is here"
    except KeyError:
        request.session['history'] = []
    print "made it"
    houseDict['dictWord'] = (request.POST['name'])
    houseDict['color'] = (request.POST['color'])
    houseDict['date'] = datetime.now().strftime("%Y/%m/%d at %I:%m:%p")
    houseDict['size'] = 'small'
    print  "size " + houseDict['size']
    if 'fonts' in request.POST:
        houseDict['size'] = request.POST['fonts']
    print  "size " + houseDict['size']
    # if (request.POST['fonts']):
    #     houseDict['size'] = request.POST['fonts']
    # houseDict['size'] = 'small'
    request.session['history'].append(houseDict)

    
    request.session.modified = True    
    return redirect('/session_words')

def clear(request):
    request.session.clear()
    return redirect('/session_words')


    