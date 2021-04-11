import json
from rest_framework.serializers import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import authenticate, get_user_model

from accounts.serializers import UserSerializer


User = get_user_model()


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        payload = json.loads(request.body)
        username = payload['username']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise ValidationError({'Not found': f'User with {username} does not exist'})
        user = authenticate(request, **payload)
        if user:
            return Response(UserSerializer(user).data)
        raise ValidationError({'Incorrect password': 'Could not log in user'})
