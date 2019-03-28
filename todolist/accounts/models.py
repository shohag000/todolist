from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import (
        BaseUserManager,AbstractBaseUser
        )
USERNAME_REGEX = "^[a-zA-Z0-9_.-]+$"


class MyUserManager(BaseUserManager):
    def create_user(self,username,email,password=None):
        if not email:
            raise ValueError("User must have an email address")
        user = self.model(
            username = username,
            email = self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username,email,password=None):
        user = self.create_user(username,email,password=password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    username = models.CharField(
        max_length=300,
        validators= [
            RegexValidator(regex=USERNAME_REGEX,
                           message="Username must be alphanumeric or contains number",
                           code="Invalid user name")
        ],
        unique=True
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name="Email Address"
    )
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    @property
    def is_superuser(self):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    objects = MyUserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']