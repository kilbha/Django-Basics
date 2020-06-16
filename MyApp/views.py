from django.shortcuts import render

# Create your views here.
def HomeView(request):
    return render(request,'MyTemp/home.html')
def IndexView(request):
    return render(request,'MyTemp/Index.html')