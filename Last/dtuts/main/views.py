from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # Render the home.html template
