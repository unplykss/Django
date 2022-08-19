from django.shortcuts import render, HttpResponse
from .models import Client

def contacts(request):
    return HttpResponse("<h1>Тел.: 45638658938   ||  0555157272 ||  098346667</h1>")

def info(request):
    return render(request, "info.html")

def clients_list(request):
    context = {}
    bottles_list = Client.objects.all()
    context["clients_list"] = bottles_list
    html_page = render(request, 'clients.html', context)
    return html_page