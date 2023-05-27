from django.shortcuts import render, redirect
from .models import Client
from .forms import ClientForm

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('client_listing')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('client_listing')
    else:
        form = ClientForm()
    return render(request, 'create_client.html', {'form': form})

def client_listing(request):
    clients = Client.objects.all()
    return render(request, 'client_listing.html', {'clients': clients})
    