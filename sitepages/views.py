from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def contact_page(request):
    return render(request, 'contact_page.html')

def about_me(request):
    return render(request, 'about.html')