from django.shortcuts import render

def home_view(request):
    return render(request, 'website/index.html')

def contact_view(request):
    return render(request, 'website/contact.html')

def about_view(request):
    return render(request, 'website/about.html')
