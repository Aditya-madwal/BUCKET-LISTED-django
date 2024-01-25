from django.shortcuts import render, redirect
from .forms import user_registeration_form
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .models import item

from .brain import *

# Create your views here.

def loginview(request) :
    if request.user.is_authenticated :
        return redirect(homeview)
    else :
		# not logged in
        if request.method == 'POST' :
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username = username, password = password)

            if user is not None :
                # login into the website
                login(request, user)
                return redirect(homeview)
            else :
            # authentication failed
                messages.info(request, 'invalid login')
                return redirect(loginview)
            
    # return redirect(loginview)
    return render(request, 'login.html', {})
    

@login_required(login_url=loginview)
def homeview(request) :

    item_list = item.objects.filter(shopper = request.user)

    context = {
        "items" : item_list,
    }

    if request.method == "POST" :
        link = request.POST['link']
        # print(link)
        for i in range(0,3) :
            item_data_obj = get_data(link)
            pass
        name = item_data_obj['title']
        price = item_data_obj['price']
        shopper = request.user
        status = 0

        new_item = item(link = link, name = name, price = price, status = status, shopper = shopper)
        new_item.save()

    return render(request, 'home.html', context = context)


def signupview(request) :
    form = user_registeration_form(request.POST)

    context = {
        'form' :form,
    }

    if request.user.is_authenticated is False :
        if request.method == 'POST' :
            if form.is_valid() :
                form.save()
            return redirect(loginview)
    else :
        return redirect(homeview)
    return render(request, 'signup.html', context=context)

def historyview(request) :
    return render(request, 'history.html', {})

def logoutview(request) :
    logout(request)
    return redirect(loginview)