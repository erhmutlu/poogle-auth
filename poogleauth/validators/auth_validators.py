from django.contrib.auth import authenticate
from rest_framework import serializers, exceptions

__author__ = 'erhmutlu'


class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise exceptions.ValidationError("username or password is incorrect!")

            attrs['user'] = user
            return attrs