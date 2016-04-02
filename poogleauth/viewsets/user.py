from django.contrib.auth import get_user_model
from poogleauth.serializers import UserDetailsSerializer, UserSerializer
from poogleauth.viewsets.base import BaseModelWithPaginationViewSet

__author__ = 'erhmutlu'


class UserViewSet(BaseModelWithPaginationViewSet):
    User = get_user_model()
    model = User
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            serializer = UserDetailsSerializer
        else:
            serializer = UserSerializer
        return serializer


