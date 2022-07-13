from django.urls import path
from .views import index, about, website_log

urlpatterns = [
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('website_log/', website_log, name='website_log'),
]
