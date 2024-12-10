from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request,'login.html')

def registeratoin(request):
    return render(request,'registeration.html')