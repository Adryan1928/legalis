from django.urls import path, include
from . import views
from django.contrib.auth.urls import views as auth_views

app_name = 'user'

urlpatterns = [
    path('', views.landingPage, name='landing_page'),
    # path('login/', views.login, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]