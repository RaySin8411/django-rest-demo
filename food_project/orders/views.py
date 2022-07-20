from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .tests import ecpay_payment_test, ecpay_logistic_test



# Create your views here.
@csrf_exempt
def ecpay_payment_view(request):
    return HttpResponse(ecpay_payment_test())


@csrf_exempt
def ecpay_logistic_view(request):
    return HttpResponse(ecpay_logistic_test())

