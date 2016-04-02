from django.contrib.auth.models import BaseUserManager
from django.utils import timezone

__author__ = 'erhmutlu'


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, first_name, last_name,
                     is_superuser, **extra_fields):

        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_active=True,
                          is_superuser=is_superuser,
                          first_name=first_name.title(),
                          last_name=last_name.title(),
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username,  email, password, first_name, last_name, **extra_fields):
        return self._create_user(username, email, password, first_name, last_name, False,
                                 **extra_fields)

    def create_superuser(self, username, email, password, first_name, last_name, **extra_fields):
        return self._create_user(username, email, password, first_name, last_name, True,
                                 **extra_fields)