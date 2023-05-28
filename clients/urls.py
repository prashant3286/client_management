from django.urls import path
from . import views

app_name = 'your_app_name'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('create-client/', views.create_client, name='create_client'),
    path('client-listing/', views.client_listing, name='client_listing'),
    path('signup/', views.signup, name='signup'),
]
