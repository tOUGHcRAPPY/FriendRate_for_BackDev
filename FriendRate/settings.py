"""
Django settings for FriendRate project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-p3d=x0ta6$ko=7py5qz@_+#&clin+(@t2y2yvzr4drf^5&)v4)"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.sites",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "user",
    "social_django",
    "rest_framework",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.facebook",
    "allauth.socialaccount.providers.google",
]

SITE_ID = 1

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "FriendRate.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

WSGI_APPLICATION = "FriendRate.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


AUTH_USER_MODEL = "user.User"
ACCOUNT_FORMS = {
    "add_email": "allauth.account.forms.AddEmailForm",
    "change_password": "allauth.account.forms.ChangePasswordForm",
    "login": "allauth.account.forms.LoginForm",
    "reset_password": "allauth.account.forms.ResetPasswordForm",
    "reset_password_from_key": "allauth.account.forms.ResetPasswordKeyForm",
    "set_password": "allauth.account.forms.SetPasswordForm",
    "signup": "allauth.account.forms.SignupForm",
    "user_token": "allauth.account.forms.UserTokenForm",
}

ACCOUNT_AUTHENTICATION_METHOD = ("email",)
ACCOUNT_ALLOW_REGISTRATION = True
ACCOUNT_EMAIL_VERIFICATION = ("mandatory",)
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False


SOCIALACCOUNT_PROVIDERS = {
    "facebook": {
        "SCOPE": ["email"],
        "METHOD": "oauth2",
        "VERIFIED_EMAIL": False,
        "FIELDS": [
            "id",
            "email",
            "name",
            "first_name",
            "last_name",
            "verified",
            "locale",
            "timezone",
            "link",
            "gender",
            "updated_time",
        ],
        "EXCHANGE_TOKEN": True,
        "APP": {
            "client_id": "362713409645033",
            "secret": "e11a812f6bd660e74a5b9eb59c1dae66",
            "key": "",
        },
    },
    "google": {
        "SCOPE": ["profile", "email"],
        "AUTH_PARAMS": {"access_type": "online"},
        "APP": {
            "client_id": "722867581498-ubd170nabskvdegqncpe5qaajsja5bbp.apps.googleusercontent.com",
            "secret": "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",
            "key": "",
        },
    },
}

