import json
from rest_framework.serializers import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import authenticate, get_user_model, login
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect

from accounts.serializers import UserSerializer


User = get_user_model()


class LoginView(APIView):
    @method_decorator(csrf_protect)
    def post(self, request, *args, **kwargs):
        payload = request.data
        username = payload['username']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise ValidationError({'error': f'User with username {username} was not found'})
        user = authenticate(request, **payload)
        if user:
            login(request, user)
            return Response(UserSerializer(user).data)
        raise ValidationError({'error': 'Invalid Password'})
