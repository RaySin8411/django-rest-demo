from django.urls import path
from .views import ecpay_view

urlpatterns = [
  path('ecpay/test_order', ecpay_view, name="ecpay_payment")
]
