from django.shortcuts import render# Create your views here.

def index( request):
    return render(request, 'index.html')


def request_google_api( request):

    text = {
        'text':request.POST['text'].replace(' ' , '+')
    }
    return render(request, 'ok.html' ,  text)