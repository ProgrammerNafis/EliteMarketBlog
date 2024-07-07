from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import *


def sign_up(request):
    return render(request,'al/signup.html')