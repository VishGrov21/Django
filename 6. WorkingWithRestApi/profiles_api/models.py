from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class UserProfileManager (BaseUserManager):
    """ Manges the User Profiles """

    def create_user(self, name, email, password=None):
        """ New User Profile """
        if not email:
            raise ValueError('User must have an email address ')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, name, email, password):
        """ Creates the Super User"""
        user = self.create_user(name, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class UserProfile (AbstractBaseUser, PermissionsMixin):
    """ Database model for users in the system """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIREDFIELDS = ['name']

    def get_fullname(self):
        """ Retrieve Full Name of the user """
        return self.name

    def get_shortname(self):
        """ Retrieve Short Name of the user """
        return self.name

    def __str__(self):
        """ Returns the String Representation of the User """
        return self.email
