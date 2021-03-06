from django.urls import path, include
from django.urls.resolvers import URLPattern
from .views import LoginView, LogoutView

urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='auth_login'),
    path('auth/logout/', LogoutView.as_view(), name='auth_logout'),
]