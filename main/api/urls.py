from django.urls import path
from .views import index, request_google_api

urlpatterns = [
    path('' , index ),
    path('form/' ,  request_google_api)
]

#https://www.googleapis.com/books/v1/volumes?q=flowers+inauthor:keyes