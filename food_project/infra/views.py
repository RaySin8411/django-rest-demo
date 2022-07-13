from django.shortcuts import render


# Create your views here.
def index(request):
    templates = 'infra/index.html'
    return render(request, templates, locals(), )


def about(request):
    templates = 'infra/about.html'
    return render(request, templates, locals(), )
