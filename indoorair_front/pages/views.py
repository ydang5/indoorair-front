from rest_framework import status, response, views
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect

def index_page(request):
    user = request.user

    return render(request,'pages/index.html',{})



def contact_page(request):
        context = {}

        return render(request,'pages/contact.html',context)
