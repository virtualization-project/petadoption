from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'about-us.html')

def contact(request):
    return render(request, 'contacts.html')

def adoption(request):
    return render(request, 'blog.html')

def adminlogin(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def services(request):
    return render(request, 'services.html')