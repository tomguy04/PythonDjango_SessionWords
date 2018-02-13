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
    request.session['history'].append(houseDict)

    # if 'history' not in request.session.keys():
    #     request.session['history'] = []
    # print "this line"        
    # houseDict['dictWord'] = (request.POST['name'])
    # request.session['history'].append(request.POST['name'])
    # print "**********************history->"+str(request.session['history'])
    # return redirect('/session_words')
        
    # if 'history' in request.session.keys():
    #     houseDict['dictWord'] = (request.POST['name'])
    #     houseDict['color'] = (request.POST['color'])
    #     houseDict['date'] = datetime.now().strftime("%Y/%m/%d at %I:%m:%p")
    #     request.session['history'].append(houseDict)
    #     print "**********************MOREhistory->"+str(request.session['history'])
        
    # else:
    #     houseDict['dictWord'] = (request.POST['name'])
    #     houseDict['date'] = datetime.now().strftime("%Y/%m/%d at %I:%m:%p")
    #     request.session['history'] = []
    #     request.session['color'] = request.POST['color']
    #     request.session['history'].append(request.POST['name'])
    #     print "**********************history->"+str(request.session['history'])
    request.session.modified = True    
    return redirect('/session_words')

def clear(request):
    request.session.clear()
    return redirect('/session_words')


    