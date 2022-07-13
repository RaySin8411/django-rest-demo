from django.http import HttpResponse
from django.shortcuts import redirect


# Create your views here.
def hello(request):
    return redirect('/api/index')


def view_404(request, exception=None):
    # make a redirect to homepage
    # you can use the name of url or just the plain link
    return redirect('/')
