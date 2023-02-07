"""labexpress URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView,
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,
    PasswordResetCompleteView, logout_then_login
)


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/password_change/',
         PasswordChangeView.as_view(), name='password_change'),
    path('accounts/password_change/done/',
         PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('accounts/password_reset/',
         PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/',
         PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
