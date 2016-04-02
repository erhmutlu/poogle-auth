from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from poogleauth.views.authentication import Login, Logout
from poogleauth.viewsets.user import UserViewSet

__author__ = 'erhmutlu'

router = DefaultRouter()
router.register(r'User', UserViewSet, base_name="user")

urlpatterns = [
                url(r'api/', include(router.urls)),
                url(r'^api/auth/login/$', Login.as_view(), name='rest-login'),
                url(r'^api/auth/logout/$', Logout.as_view(), name='rest-logout'),

]
