from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView

from . import views

app_name = 'visitor'

# Only the homepage is live for now. The other pages redirect to it until
# they are redesigned; to bring one back, swap its redirect for the original
# route listed below.
#   path('about/', views.AboutView.as_view(), name='about'),
#   path('services/', views.ServicesView.as_view(), name='services'),
#   path('detail/<str:identifier>/', views.DetailView.as_view(), name='detail'),
#   path('contact/', views.ContactView.as_view(), name='contact'),
home = RedirectView.as_view(url=reverse_lazy('visitor:index'), permanent=False)

urlpatterns = [
        path('', views.IndexView.as_view(), name='index'),
        path('about/', home, name='about'),
        path('services/', home, name='services'),
        path('detail/<str:identifier>/', home, name='detail'),
        path('contact/', home, name='contact'),
        ]
