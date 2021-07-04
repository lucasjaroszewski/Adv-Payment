from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView

urlpatterns = [
    path('user-register/', RegisterView.as_view(), name='user-register'),
    path('user-login/', LoginView.as_view(), name='user-login'),
    path('user-logout/', LogoutView.as_view(), name='user-logout'),
    path('user-token/', UserView.as_view(), name='user-token')
]
