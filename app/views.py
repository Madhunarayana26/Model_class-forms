from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
def insert_topic(request):
    TMFO=TopicModelForm()
    d={'TMFO':TMFO}
    if request.method=='POST':
        TMFD=TopicModelForm(request.POST)
        if TMFD.is_valid():
            TMFD.save()
            return HttpResponse('Data inserted')
    return render(request,'insert_topic.html',d)
def insert_webpage(request):
    WMFO=WebpageModelForm()
    d={'WMFO':WMFO}
    if request.method=='POST':
        WMFD=WebpageModelForm(request.POST)
        if WMFD.is_valid():
            WMFD.save()
            return HttpResponse('Data inserted')
        else:
            return HttpResponse('<i>please enter a valid data</i>')
    return render(request,'insert_Webpage.html',d)

def insert_accessrecord(request):
    AMFO=AccessRecordModelForm()
    d={'AMFO':AMFO}
    if request.method=='POST':
        AMFD=AccessRecordModelForm(request.POST)
        if AMFD.is_valid():
            AMFD.save()
            return HttpResponse('Data inserted')
        else:
            return HttpResponse('<i>please enter a valid data</i>')

    return render(request,'insert_accessrecord.html',d)















