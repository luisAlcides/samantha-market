import yfinance as yf

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .models import User
from .forms import UserForm, MyUserCreationForm

from django.utils.translation import activate



# Create your views here.
def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exit')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    return render(request, 'base/home.html', {})


def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'base/login_register.html', {'form': form})


@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)

    return render(request, 'base/update-user.html', {'form': form})




# def activos(request):
#     symbols = obtener_simbolos_disponibles()
#     stocks = []
#     cards_data = []

#     for symbol in symbols:
#         stocks.append(yf.Ticker(symbol))

#     for stock in stocks:
#         symbol = stock.info['symbol']
#         price = round(stock.history().tail(1)["Close"].iloc[0], 4)
#         num_purchases = obtener_num_compras(symbol) 
#         cards_data.append({'title': symbol, 'price': price, 'num_purchases': num_purchases})

#     cards_data.sort(key=lambda x: x['num_compras'], reverse=True)

#     return render(request, 'base/activos.html', {'cards_data': cards_data})


import yfinance as yf
import pandas as pd

def activos(request):
    details = None
    most_active_data = {}

    if request.method == 'POST':
        symbol = request.POST.get('symbol')
        stock = yf.Ticker(symbol)

        if 'longName' in stock.info:
            name = stock.info['longName']
        else:
            name = 'Nombre no disponible'

        details = {
            'symbol': stock.info.get('symbol'),
            'name': name,
            'price': round(stock.history().tail(1)['Close'].iloc[0], 4),
            'country': stock.info['country'],
            'marketCap': stock.info['marketCap'],
            
        }

    symbols = ['AAPL', 'MSFT', 'AMZN']
    stocks = []
    most_active_data = []

    for symbol in symbols:
        stocks.append(yf.Ticker(symbol))

    for stock in stocks:
        symbol = stock.info['symbol']
        price = round(stock.history().tail(1)["Close"].iloc[0], 4)
        most_active_data.append({'title': symbol, 'price': price})
        
    return render(request, 'base/activos.html', {'details': details, 'most_active_data': most_active_data})





def detalle_accion(request, symbol):
    stock = yf.Ticker(symbol)
    
    activate('es')
    
    context = {
        'symbol': stock.info['symbol'],
        'name': stock.info['longName'],
        'website': stock.info['website'],
        'country': stock.info['country'],
        'sector': stock.info['sector'],
        'longBusinessSummary': stock.info['longBusinessSummary'],
        'marketCap': stock.info['marketCap'],
        'price': stock.history().tail(1)['Close'].iloc[0],
        
    }
    
    return render(request, 'base/detalle_accion.html', context)


def blog(request):
    return render(request, 'base/blog.html', {})

def trading(request):
    return render(request, 'base/blog.html', {})