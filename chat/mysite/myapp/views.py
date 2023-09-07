from django.shortcuts import render, redirect

def home(request):
    return render(request,'home.html')

def hello(request):
    return render(request,'hello.html')

def cartype(request):
    if request.method == 'POST':
        date = request.POST.getlist('date')
        time = request.POST.getlist('time')
        options = request.POST.getlist('options')

    if 'cartype' in options and len(options) == 1:
        return redirect('cartype')
   

# Create your views here.
