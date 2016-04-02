from django.contrib.auth import get_user_model
from rest_framework import serializers

__author__ = 'erhmutlu'


class UserDetailsSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """

    class Meta:
        model = get_user_model()
        exclude = ('password',)

        depth = 1
