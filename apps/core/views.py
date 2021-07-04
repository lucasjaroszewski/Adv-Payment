from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models.functions import Extract, Trunc, Now
from django.db.models import F, Sum
from django.db import models
from django.db.models import Q
from django.views.generic import View
from apps.users.models import User, Payment
from apps.core.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
import datetime


def home(request):
    return render(request, 'core/home.html')

def register(request):
    '''
        Forms.py

    '''

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# Login_required decorator to prevent anonymous accessing dashboard
@login_required
def dashboard(request):

    # Filter for payments
    payments = Payment.objects.filter(user=request.user)

    if request.GET.get('sorting'):
        featured_filter = request.GET.get('sorting')
        payments = Payment.objects.filter(payment_status=featured_filter).filter(user=request.user)

    elif request.GET.get(''):
        payments = Payment.objects.filter(user=request.user)

    else:
        payments = Payment.objects.filter(user=request.user)

    # All front-end related codes are handled in models.py
    context = {
        'payments': payments.order_by('-date_added'),
    }

    return render(request, 'core/dashboard.html', context)

@login_required
def dashboard_add(request):
    return render(request, 'core/dashboard_add.html')

@staff_member_required
def dashboard_admin(request):

    # Filter for payments
    payments = Payment.objects.filter(payment_status='Pending')

    if request.GET.get('sorting'):
        featured_filter = request.GET.get('sorting')
        payments = Payment.objects.filter(payment_status=featured_filter)

    elif request.GET.get(''):
        payments = Payment.objects.all()

    else:
        payments = Payment.objects.filter(payment_status='Pending')

    # All front-end related codes are handled in models.py
    context = {
        'payments': payments.order_by('-date_added'),
    }

    return render(request, 'core/dashboard_admin.html', context)

@staff_member_required
def dashboard_admin_add(request):
    return render(request, 'core/dashboard_admin_add.html')
