from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from apps.core import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.home, name='home'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('dashboard/admin', user_views.dashboard_admin, name='dashboard-admin'),
    path('dashboard/admin/add', user_views.dashboard_admin_add, name='dashboard-admin-add'),
    path('dashboard/', user_views.dashboard, name='dashboard'),
    path('dashboard/add', user_views.dashboard_add, name='dashboard-add'),
    path('api/', include('api.urls')),
]
