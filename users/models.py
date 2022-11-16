from django.conf import settings
from django.contrib.auth.models import AbstractUser, AnonymousUser
from questions.models import Category

from django.db.models import (
    CASCADE,
    CharField,
    DateTimeField,
    ForeignKey,
    ManyToManyField,
    Model,
    TextField,
)

#####
from django.contrib.auth.models import AbstractUser, AnonymousUser
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _

from django.db.models.manager import EmptyManager

from django.contrib import auth
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.db import models
from django.db.models.manager import EmptyManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

###




# class User(AbstractUser):

#     followers = ManyToManyField('self', related_name='followees', symmetrical=False)
#     mobile_number=CharField(max_length=255,default="020")
#     language_prefered=CharField(max_length=255,default="en")
#     cat_prefered=ForeignKey(Category, related_name='prefered_category', default=1, on_delete=CASCADE)






 
           
class Useranonymous(AnonymousUser):
    id = 345
    pk = None
    username = 'anonymous'
    is_staff = False
    is_active = False
    is_superuser = False
    language_prefered="dari"

    def __str__(self):
        return 'AnonymousUser'

    def __eq__(self, other):
        return isinstance(other, self.__class__)

    def __hash__(self):
        return 1  # instances always return the same hash value

    def __int__(self):
        raise TypeError('Cannot cast AnonymousUser to int. Are you trying to use it in place of User?')

    def save(self):
        raise NotImplementedError("Django doesn't provide a DB representation for AnonymousUser.")

    def delete(self):
        raise NotImplementedError("Django doesn't provide a DB representation for AnonymousUser.")

    def set_password(self, raw_password):
        raise NotImplementedError("Django doesn't provide a DB representation for AnonymousUser.")

    def check_password(self, raw_password):
        raise NotImplementedError("Django doesn't provide a DB representation for AnonymousUser.")







    def get_group_permissions(self, obj=None):
        return set()


    @property
    def is_anonymous(self):
        return True

    @property
    def is_authenticated(self):
        return False

    def get_username(self):
        return self.username

##########






class CustomUserManager(BaseUserManager):
    """custom user manager class"""
    use_in_migration = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email,mobil, password, **extra_fields)


class User(AbstractUser):
    """ Custom user model class"""

  
    language_prefered=CharField(_('language_prefered'),max_length=255,default="en")
    cat_prefered=ForeignKey(Category, related_name='prefered_category', default=1, on_delete=CASCADE)
    email = models.EmailField(_('email'), unique=True, default='')
    name = models.CharField(_('name'), max_length=50, blank=False)
    mobil = models.BigIntegerField(_('mobil'),  default=123134, blank=True)
    username = models.CharField(_('name'), max_length=50, blank=False)

    is_superadmin = models.BooleanField(_('is_superadmin'), default=False)
    is_active = models.BooleanField(_('is_active'), default=True)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    objects = CustomUserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        """stirng representation"""
        return self.username






##########
