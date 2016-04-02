from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from rest_framework import serializers

__author__ = 'erhmutlu'


class UserSerializer(serializers.ModelSerializer):
    User = get_user_model()
    groups = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), many=True, required=False)
    user_permissions = serializers.PrimaryKeyRelatedField(queryset=Permission.objects.all(), many=True,
                                                          required=False)

    string_value = serializers.SerializerMethodField('to_string')
    id = serializers.SerializerMethodField('id_value')

    def to_string(self, obj):
        return str(obj)

    def id_value(self, obj):
        return obj.id

    class Meta:
        model = get_user_model()
        depth = 2