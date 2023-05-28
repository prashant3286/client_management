from django.urls import path
from . import views

app_name = 'your_app_name'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('create-client/', views.create_client, name='create-client'),
    path('client-listing/', views.client_listing, name='client-listing'),
    path('signup/', views.signup, name='signup'),
]
