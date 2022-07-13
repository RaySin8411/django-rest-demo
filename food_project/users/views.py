from datetime import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework import generics

from .forms import CustomerUserCreateForm
from .serializers import UserSerializer

suffix = 'user/'


# Create your views here.
class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


@login_required
def dashboard(request):
    username = request.user.first_name
    templates = suffix + 'dashboard.html'
    return render(request, templates, locals())


def registration(request):
    if request.method == 'POST':
        user_form = CustomerUserCreateForm(request.POST or None)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password1']
            )
            new_user.save()
            templates = suffix + 'register_done.html'
            return render(request, templates, locals())
        else:
            user_form = CustomerUserCreateForm()
            templates = suffix + 'registration.html'
            if UserCreationForm.error_messages:
                error_msg = UserCreationForm.error_messages
            return render(request, templates, locals(), )
    else:
        templates = suffix + 'registration.html'
        user_form = CustomerUserCreateForm()
        templates = suffix + 'registration.html'
        return render(request, templates, locals(), )
