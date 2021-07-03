from django.urls import path, include
from api import views

urlpatterns = [
    path('', views.apiOverview, name="overview"),
    path('payment-create/', views.paymentCreate, name="payment-create"),
    path('payment-list/', views.paymentList, name="payment-list"),
    path('payment-update/<str:id>/', views.paymentUpdate, name="payment-update"),
    path('payment-delete/<str:id>/', views.paymentDelete, name="payment-delete"),
]
