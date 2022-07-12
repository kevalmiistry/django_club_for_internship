from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'bs_home.html')

def records(request):
    return render(request, 'bs_table.html')