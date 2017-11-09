from django.shortcuts import render


def homepage(request):
    return render(request, 'main/homepage.html', {})

def whyla(request):
    return render(request, 'main/whyla.html', {})

def process(request):
    return render(request, 'main/process.html', {})

def aboutus(request):
    return render(request, 'main/aboutus.html', {})