from django.urls import path
from .views import home, profile, OtpView, RegisterView

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
#    path('otp/', OtpView.as_view(), name='otp'),
]
