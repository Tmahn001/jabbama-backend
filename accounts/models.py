from django.db import models
from django.contrib.auth.models import UserManager as BaseUserManager, AbstractUser
#from phonenumber_field.modelfields import PhoneNumberField
#from api.models import Property, Flat, AddPayment
from tabnanny import verbose
from django.dispatch import receiver
from django.urls import reverse
#from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail 

# Create your models here.

'''class UserManager(BaseUserManager):
    """ User Manager that knows how to create users via email instead of username """
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

USER_TYPE = (('admin', 'admin'), ('customer', 'customer'))

class User(AbstractUser):
    #objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    username = None
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    #user_type = models.CharField(max_length=10, choices=USER_TYPE)

    def __str__(self):
        return str(self.email)'''