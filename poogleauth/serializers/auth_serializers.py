from rest_framework import serializers
from rest_framework.authtoken.models import Token
from poogleauth.validators.auth_validators import AuthTokenSerializer

__author__ = 'erhmutlu'


class LoginSerializer(AuthTokenSerializer):
    pass


class TokenSerializer(serializers.ModelSerializer):
    """
    Serializer for Token model.
    """

    class Meta:
        model = Token
        fields = ('key',)