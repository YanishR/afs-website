from django.urls import path, include

from . import views

app_name = 'visitor'

urlpatterns = [
        path('', views.IndexView.as_view(), name='index'),
        path('about/', views.AboutView.as_view(), name='about'),
        path('services/', views.ServicesView.as_view(), name='services'),
        path('detail/<str:identifier>/', views.DetailView.as_view(), name='detail'),
        path('contact/', views.ContactView.as_view(), name='contact'),
        ]
