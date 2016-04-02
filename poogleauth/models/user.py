from django.contrib.auth.models import AbstractBaseUser, AbstractUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from poogleauth.managers.user import UserManager

__author__ = 'erhmutlu'

MALE = 1
FEMALE = 2
GENDER_CHOICES = ((MALE, "MALE"), (FEMALE, "FEMALE"))


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(verbose_name='username', unique=True, null=False, blank=False, max_length=20)
    email = models.EmailField(verbose_name='email', unique=True, null=False, blank=False)
    first_name = models.CharField(verbose_name='first name', max_length=30, null=False, blank=False)
    last_name = models.CharField(verbose_name='last name', max_length=30, null=False, blank=False)
    gender = models.IntegerField(verbose_name='gender', choices=GENDER_CHOICES, null=True)
    age = models.IntegerField(verbose_name='age', null=True)

    is_active = models.BooleanField(_('active'), default=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    objects = UserManager()

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    class Meta:
        db_table = 'poogleauth_user'