from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def men_page(request):
    return render(request, 'men.html')

def women_page(request):
    return render(request, 'women.html')

def kids_page(request):
    return render(request, 'kids.html')

def eid_collection(request):
    return render(request, 'eid.html')

def contact(request):
    return render(request, 'contact.html')
