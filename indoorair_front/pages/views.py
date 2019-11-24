from rest_framework import status, response, views
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect


# ---- homepage -----

def index_page(request):
    user = request.user

    return render(request,'pages/index.html',{})



def contact_page(request):
        context = {}

        return render(request,'pages/contact.html',context)

#----gateway----

def register_page(request):
   return render(request, "pages/gateway/register.html", {})



def register_ok_page(request):
    return render(request, "pages/gateway/register_ok_page.html",{})


def login_page(request):
   user = request.user
   return render(request, "pages/gateway/login.html", {})



def logout_page(request):
   user = request.user
   return render(request, "pages/gateway/logout.html", {})


#---dashboard---


def dashboard_page(request):
    user = request.user


    if user.is_authenticated == False:
        return HttpResponse("Cannot view page - you must login first")

    context = {
        'user': user,
    }
    return render(request,'dashboard/dashboard.html',context)


# ---instrument ---

def i_list_page(request):
    return render(request, "pages/instrument/list.html", {})


def i_retrieve_page(request, id):
    return render(request, "pages/instrument/retrieve.html", {
        "instrument_id": int(id),
    })


def i_update_page(request, id):
    return render(request, "pages/instrument/update.html", {
        "instrument_id": int(id),
    })


#---user profile---


def profile_retrieve_page(request):
    return render(request, "userprofile/retrieve.html", {})



def profile_update_page(request):
    return render(request, "userprofile/update.html", {})

#---report---


def report_list_page(request):
    return render(request,"report/list.html",{})


def report_01_page(request):
    return render(request,"report/01.html",{})


def sensor_retrieve_page(request, id):
    return render(request, "sensor/retrieve.html", {
        "sensor_id": int(id),
    })
