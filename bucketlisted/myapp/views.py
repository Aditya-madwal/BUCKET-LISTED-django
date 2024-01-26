from django.shortcuts import render, redirect
from .forms import user_registeration_form
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages

from .models import item

from .amzn import *

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
    return render(request, 'login.html')
    

@login_required(login_url=loginview)
def homeview(request) :

    item_list = item.objects.filter(shopper = request.user, status = 0)

    context = {
        "items" : item_list,
    }

    if request.method == "POST" :
        link = request.POST['link']
        item_object = get_product_data(link)

        if item.objects.filter(name = item_object['name']) :
            # messages.error(request, "already exists in the bucket")
            return redirect(homeview)

        new_item = item(link = link, name = item_object['name'], price = item_object['price'], status = 0,shopper = request.user, imgsrc = item_object['img_src'])
        new_item.save()
        # messages = None
        return redirect(homeview)

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

@login_required(login_url = loginview)
def historyview(request, user) :
    item_list = item.objects.filter(shopper = request.user, status = 1)

    if len(item_list) == 0 :
        # messages.info(request, 'this section is empty')
        pass

    context = {
        'items' : item_list,
    }

    return render(request, 'history.html', context)



def logoutview(request) :
    logout(request)
    return redirect(loginview)


@login_required(login_url = loginview)
def orderedview(request, user, itemid) :
    item_data = item.objects.get(id = itemid)

    if request.method == "POST" :
        # STOP TRACKING THE ITEM
        # status = 1
        item_data.status = 1
        item_data.save()
        return redirect(homeview)
    return render(request, 'ordered.html', {'item':item_data})


@login_required(login_url = loginview)
def deleteview(request, user, itemid) :
    if item.objects.get(id = itemid).shopper == request.user :
        # jain win request
        item_data = item.objects.get(id = itemid)

        if request.method == "POST" :
            item.objects.get(id = itemid).delete()
            return redirect(homeview)
        return render(request, 'delete.html', {'item':item_data})
    else :
        # golmaal hai sab golmaal hai
        print("backchodi mat kr")

        return redirect(homeview)
