from django.shortcuts import render, redirect
from django.core.paginator import Paginator
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
    search_query = request.GET.get('search_query')
    clients = Client.objects.all()

    if search_query:
        clients = clients.filter(name__icontains=search_query)

    paginator = Paginator(clients, 10)  # Display 10 clients per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'client_listing.html', {'page_obj': page_obj, 'search_query': search_query})


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return render(request, 'login.html')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})
