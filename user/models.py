from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


class Gender(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class User(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = [
        ("M", "Men"),
        ("W", "Women"),
        ("NB", "Enby"),
    ]
    username = models.CharField(max_length=50, unique=True, null=False)
    password = models.CharField(max_length=128)  # TODO Django's make_password
    email = models.EmailField(max_length=150, unique=True, null=False)
    name = models.CharField(max_length=50, null=True)
    surname = models.CharField(max_length=50, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    birth_date = models.DateField(null=True)
    avatar = models.ImageField(upload_to="avatars/", null=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, null=True)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


def get_by_natural_key(self, username):
    return self.get(**{f"{self.model.USERNAME_FIELD}__iexact": username})


class PasswordReset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reset_code = models.CharField(max_length=50)
    expiration_date = models.DateTimeField()


class LoginAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class LoginHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class PasswordRecovery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recovery_code = models.CharField(max_length=50)
    expiration_date = models.DateTimeField()


