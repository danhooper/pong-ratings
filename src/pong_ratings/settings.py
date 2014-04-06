# -*- coding: utf-8 -*-
# Django settings for zero project.

import os.path
import posixpath

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# tells Pinax to serve media through the staticfiles app.
SERVE_MEDIA = DEBUG

# django-compressor is turned off by default due to deployment overhead for
# most users. See <URL> for more information
COMPRESS = False

INTERNAL_IPS = [
    "127.0.0.1",
]

ADMINS = [
    # ("Your Name", "your_email@domain.com"),
]

MANAGERS = ADMINS

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3", # Add "postgresql_psycopg2", "postgresql", "mysql", "sqlite3" or "oracle".
        "NAME": os.path.join(PROJECT_ROOT, "dev.db"), # Or path to database file if using sqlite3.
        "USER": "", # Not used with sqlite3.
        "PASSWORD": "", # Not used with sqlite3.
        "HOST": "", # Set to empty string for localhost. Not used with sqlite3.
        "PORT": "", # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "US/Eastern"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"

SITE_ID = 1
SITE_ROOT = 'pong_ratings'
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = False
# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, "site_media", "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = "/site_media/media/"

# Absolute path to the directory that holds static files like app media.
# Example: "/home/media/media.lawrence.com/apps/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")

# URL that handles the static files like app media.
# Example: "http://media.lawrence.com"
STATIC_URL = "/pong_ratings/static/"
LOGIN_URL = "/pong_ratings/accounts/login"
LOGOUT_URL = "/pong_ratings/accounts/logout"
LOGIN_REDIRECT_URL = "/pong_ratings/"

# Additional directories which hold static files
STATICFILES_DIRS = [
]


STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
#    "django.contrib.staticfiles.finders.LegacyAppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
]

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = posixpath.join(STATIC_URL, "admin/")

# Subdirectory of COMPRESS_ROOT to store the cached media files in
COMPRESS_OUTPUT_DIR = "cache"

# Make this unique, and don't share it with anybody.
SECRET_KEY = "!1t))7bgvn_vilvwhn*85cqfe*1syo*2e^izc*=9ut+usun07h"

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
]

MIDDLEWARE_CLASSES = [
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "pinax.middleware.security.HideSensistiveFieldsMiddleware",
    "account.middleware.LocaleMiddleware",
    "account.middleware.TimezoneMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "stronghold.middleware.LoginRequiredMiddleware",
]

ROOT_URLCONF = "pong_ratings.urls"

TEMPLATE_DIRS = [
    os.path.join(PROJECT_ROOT, "templates"),
    os.path.join(PROJECT_ROOT, 'apps')
]

TEMPLATE_CONTEXT_PROCESSORS = [
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",

    "pinax.core.context_processors.pinax_settings",
    "account.context_processors.account",
]

INSTALLED_APPS = [
    # Django
    "django.contrib.auth",
    "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.humanize",
    "django.contrib.staticfiles",

    "pinax.templatetags",

    # theme
    "pinax_theme_bootstrap",
    "bootstrapform",

    # external
    "compressor",
    "debug_toolbar",
    "south",
    'account',
    'stronghold',

    # Pinax

    # project
    "score",
]

FIXTURE_DIRS = [
]

MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

#EMAIL_BACKEND = "mailer.backend.DbBackend"
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
STRONGHOLD_PUBLIC_URLS = (
    r'^%s/%s.+$' % (SITE_ROOT, STATIC_URL),
    r'^%s/%s.+$' % (SITE_ROOT, MEDIA_URL),
)
STRONGHOLD_PUBLIC_NAMED_URLS = (
    'account_login',
    'account_signup',
)

DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
}

# local_settings.py can be used to override environment-specific settings
# like database and email that differ between development and production.
try:
    from local_settings import *
except ImportError:
    pass
