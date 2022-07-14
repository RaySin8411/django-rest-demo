from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .tests import ecpay_test


# Create your views here.
@csrf_exempt
def ecpay_view(request):
    return HttpResponse(ecpay_test())
