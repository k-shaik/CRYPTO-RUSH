from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.shortcuts import redirect
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy

from django.contrib.auth import authenticate

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        try:
            user = User.objects.get(username=username)
            if user.is_superuser:
                if user.check_password(password):
                    return user
            else:
                if user.check_password(password):
                    return None
        except User.DoesNotExist:
            return None
    
    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def user_can_authenticate(self, user):
        return True

    def login_success_redirect(self, request, user):
        if user.is_superuser:
            return redirect('/track')
        else:
            return redirect('/')
