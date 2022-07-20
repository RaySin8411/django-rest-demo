from django.urls import path
from .views import ecpay_payment_view, ecpay_logistic_view

urlpatterns = [
    path('ecpay/test_order_payment', ecpay_payment_view, name="ecpay_payment"),
    path('ecpay/test_order_logistic', ecpay_logistic_view, name="ecpay_logistic")

]
