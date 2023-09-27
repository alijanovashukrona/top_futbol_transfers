from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def u_20(request):
    return render(request, 'U-20 players.html')

def englad(request):
    return render(request, 'england.html')

def country(request):
    return render(request,'country-clubs.html')

def clubs(request):
    return


