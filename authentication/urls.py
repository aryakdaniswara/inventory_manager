from django.urls import path
from authentication.views import login, logout, register_flutter

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register_flutter/', register_flutter, name='register_flutter'),
]