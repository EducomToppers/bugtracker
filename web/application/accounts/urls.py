from django.urls import path

from accounts.views import RegisterView, LoginView, CSRFToken


app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('csrf-token/', CSRFToken.as_view(), name='csrf-token'),
]
