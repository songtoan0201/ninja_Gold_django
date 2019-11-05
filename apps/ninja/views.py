from django.shortcuts import render, redirect
from django import forms
import random
from datetime import datetime
# Create your views here.


def index(request):
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1

    request.session['farm_gold'] = 0
    request.session['cave_gold'] = 0
    request.session['house_gold'] = 0
    request.session['casino_gold'] = 0
    request.session['total_gold'] = 0
    return render(request, "ninja/index.html")


def reset(request):
    del request.session['farm_gold']
    del request.session['cave_gold']
    del request.session['house_gold']
    del request.session['casino_gold']
    del request.session['total_gold']
    del request.session['activities']
    return redirect('/')


def show(request):
    print(request.session['activities'])
    return render(request, "ninja/index.html")


def calculate_gold(request):
    if request.method == "POST":
        if 'activities' in request.session:
            pass
        else:
            request.session['activities'] = []
        if request.POST['which_form'] == 'farm':
            request.session['farm_gold'] = random.randint(10, 20)
            request.session['total_gold'] += request.session['farm_gold']
            request.session['activities'].append(
                f"<option style='color:green'>Earn {request.session['farm_gold']} from farming ({datetime.now().strftime('%Y/%m/%d %H:%M %p')})</option>")
        elif request.POST['which_form'] == 'cave':
            request.session['cave_gold'] = random.randint(5, 10)
            request.session['total_gold'] += request.session['cave_gold']
            request.session['activities'].append(
                f"<option style='color:green'>Earn {request.session['cave_gold']} from digging cave ({datetime.now().strftime('%Y/%m/%d %H:%M %p')})</option>")
        elif request.POST['which_form'] == 'house':
            request.session['house_gold'] = random.randint(2, 5)
            request.session['total_gold'] += request.session['house_gold']
            request.session[
                'activities'].append(f"<option style='color:green'>Earn {request.session['house_gold']} from searching house ({datetime.now().strftime('%Y/%m/%d %H:%M %p')})</option>")
        elif request.POST['which_form'] == 'casino':
            if request.session['total_gold'] > 0:
                request.session['casino_gold'] = random.randint(-50, 50)
                request.session['total_gold'] += request.session['casino_gold']
                if request.session['casino_gold'] < 0:
                    request.session[
                        'activities'].append(f"<option style='color:red'>Lose {-request.session['casino_gold']} from gambling ({datetime.now().strftime('%Y/%m/%d %H:%M %p')})</option>")

                else:
                    request.session[
                        'activities'].append(f"<option style='color:green'>Earn {request.session['casino_gold']} from gambling ({datetime.now().strftime('%Y/%m/%d %H:%M %p')})</option>")
            else:
                request.session['activities'].append(
                    f"<option style='color:red'>You have no money to enter casino ({datetime.now().strftime('%Y/%m/%d %H:%M %p')})</option>")
                request.session.modified = True
        print('I am in calculate gold')
        print('farm_gold is', request.session['farm_gold'])
        print('cave_gold is', request.session['cave_gold'])
        print('house_gold is', request.session['house_gold'])
        print('casino_gold is', request.session['casino_gold'])
        print('total_gold is', request.session['total_gold'])

    return redirect('/show')
