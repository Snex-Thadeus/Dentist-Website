from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('about.html', views.about, name="about"),
    path('services.html', views.services, name="services"),
    path('portfolio.html', views.portfolio, name="portfolio"),
    path('pricing.html', views.pricing, name="pricing"),
]