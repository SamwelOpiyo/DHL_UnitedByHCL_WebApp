"""
Django settings for dhl project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import random
import string

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = '8vp393)6p6y-$)!psi#)dm$2s9$%e6+2ayk!5vy=k4c4q^rwe0'
SECRET_KEY = os.environ.get("SECRET_KEY", "".join(random.choice(string.printable) for i in range(40)))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'dhlavenues.herokuapp.com',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    #'crispy_forms',
    #'crispy_forms_foundation',
    #'crispy_forms_foundation_demo',
    'django_xmlrpc',
    'rest_framework',
    'markdown',
    'gunicorn',
    'tagging',
    'django_comments',
    'mptt',
    'channels',
    #'tickets',
    'sorl.thumbnail',
    #'zinnia_foundation',
    #'zinnia_bootstrap',
    #'zinnia_html5',
    #'zinnia_threaded_comments',
    'zinnia',
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'admin_tools_zinnia',
    'ckeditor',
    'zinnia_ckeditor',
    'ckeditor_uploader',
    'django_bitly',
    'tweepy',
    'axes',


    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # ... include the providers you want to enable:
    #'allauth.socialaccount.providers.amazon',
    #'allauth.socialaccount.providers.angellist',
    #'allauth.socialaccount.providers.asana',
    #'allauth.socialaccount.providers.auth0',
    #'allauth.socialaccount.providers.baidu',
    #'allauth.socialaccount.providers.basecamp',
    #'allauth.socialaccount.providers.bitbucket',
    #'allauth.socialaccount.providers.bitbucket_oauth2',
    #'allauth.socialaccount.providers.bitly',
    #'allauth.socialaccount.providers.coinbase',
    #'allauth.socialaccount.providers.daum',
    #'allauth.socialaccount.providers.digitalocean',
    #'allauth.socialaccount.providers.discord',
    #'allauth.socialaccount.providers.douban',
    #'allauth.socialaccount.providers.draugiem',
    #'allauth.socialaccount.providers.dropbox',
    #'allauth.socialaccount.providers.dropbox_oauth2',
    #'allauth.socialaccount.providers.edmodo',
    #'allauth.socialaccount.providers.eveonline',
    #'allauth.socialaccount.providers.evernote',
    #'allauth.socialaccount.providers.facebook',
    #'allauth.socialaccount.providers.feedly',
    #'allauth.socialaccount.providers.fivehundredpx',
    #'allauth.socialaccount.providers.flickr',
    #'allauth.socialaccount.providers.foursquare',
    #'allauth.socialaccount.providers.fxa',
    #'allauth.socialaccount.providers.github',
    #'allauth.socialaccount.providers.gitlab',
    #'allauth.socialaccount.providers.google',
    #'allauth.socialaccount.providers.hubic',
    #'allauth.socialaccount.providers.instagram',
    #'allauth.socialaccount.providers.kakao',
    #'allauth.socialaccount.providers.line',
    #'allauth.socialaccount.providers.linkedin',
    #'allauth.socialaccount.providers.linkedin_oauth2',
    #'allauth.socialaccount.providers.mailru',
    #'allauth.socialaccount.providers.mailchimp',
    #'allauth.socialaccount.providers.naver',
    #'allauth.socialaccount.providers.odnoklassniki',
    #'allauth.socialaccount.providers.openid',
    #'allauth.socialaccount.providers.orcid',
    #'allauth.socialaccount.providers.paypal',
    #'allauth.socialaccount.providers.persona',
    #'allauth.socialaccount.providers.pinterest',
    #'allauth.socialaccount.providers.reddit',
    #'allauth.socialaccount.providers.robinhood',
    #'allauth.socialaccount.providers.shopify',
    #'allauth.socialaccount.providers.slack',
    #'allauth.socialaccount.providers.soundcloud',
    #'allauth.socialaccount.providers.spotify',
    #'allauth.socialaccount.providers.stackexchange',
    #'allauth.socialaccount.providers.stripe',
    #'allauth.socialaccount.providers.tumblr',
    #'allauth.socialaccount.providers.twentythreeandme',
    #'allauth.socialaccount.providers.twitch',
    'allauth.socialaccount.providers.twitter',
    #'allauth.socialaccount.providers.untappd',
    #'allauth.socialaccount.providers.vimeo',
    #'allauth.socialaccount.providers.vk',
    #'allauth.socialaccount.providers.weibo',
    #'allauth.socialaccount.providers.weixin',
    #'allauth.socialaccount.providers.windowslive',
    #'allauth.socialaccount.providers.xing',




    #'crispy_forms_foundation_demo',

    #'mysite.apps.MysiteConfig',
    'track.apps.TrackConfig',
    'webhook.apps.WebhookConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dhl.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n",
                "django.template.context_processors.request",
                "zinnia.context_processors.version",


                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
            ],
        },
    },
]

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgi_redis.RedisChannelLayer",
        "CONFIG": {
            "hosts": [os.environ.get('REDIS_URL', 'redis://151.80.56.184:6379')],
        },
        "ROUTING": "webhook.routing.channel_routing",
    },
}



AUTHENTICATION_BACKENDS = [

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',


]



ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQURIED=True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 3

SOCIALACCOUNT_PROVIDERS = \
    {'facebook':
       {'METHOD': 'oauth2',
        'SCOPE': ['email','public_profile', 'user_friends'],
        #'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time'],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': lambda request: 'kr_KR',
        'VERIFIED_EMAIL': True,
        'VERSION': 'v2.4'}}

WSGI_APPLICATION = 'AfricaProduce.wsgi.application'



WSGI_APPLICATION = 'dhl.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3.dhl'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'

FORCE_LOWERCASE_TAGS = True
FORCE_LOWERCASE_TAGS = 30
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.zoho.com'
EMAIL_PORT=587
EMAIL_HOST_USER='admin@samwelopiyo.guru'
EMAIL_HOST_PASSWORD='tZXr8yQJQmNq'
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL = 'admin@samwelopiyo.guru'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    'static',
]

MEDIAFILES_DIRS = [
    os.path.join(BASE_DIR, "media"),
    'media',
]


STATIC_ROOT = os.path.join(BASE_DIR, 'CollectedStatic')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'CollectedMedia')
MEDIA_URL = '/media/'

ZINNIA_UPLOAD_TO = 'uploads/zinnia'


CKEDITOR_UPLOAD_PATH = "uploads/"

SITE_ID = 1

ZINNIA_ENTRY_CONTENT_TEMPLATES = [
  ('zinnia/_short_entry_detail.html', 'Short entry template'),
]

ZINNIA_ENTRY_DETAIL_TEMPLATES = [
    ('zinnia/fullwidth_entry_detail.html', 'Fullwidth template'),
]


ZINNIA_PING_EXTERNAL_URLS = False
ZINNIA_SAVE_PING_DIRECTORIES = False

#ZINNIA_ENTRY_BASE_MODEL = 'myapp.models.Video'
ZINNIA_PAGINATION = 5

"""
ZINNIA_PING_DIRECTORIES = ['http://ping.directory.com/',
                           'http://pong.directory.com/']
"""
ZINNIA_MARKUP_LANGUAGE = 'markdown'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'comparison': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'comparison',
        'TIMEOUT': None,
   }
}



from zinnia.xmlrpc import ZINNIA_XMLRPC_METHODS
XMLRPC_METHODS = ZINNIA_XMLRPC_METHODS


ZINNIA_SPAM_CHECKER_BACKENDS = [
    'zinnia.spam_checker.backends.all_is_spam',
    'zinnia.spam_checker.backends.long_enough',
]


CKEDITOR_JQUERY_URL =  '/static/jquery.min.js'
CKEDITOR_IMAGE_BACKEND = "pillow"


CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        # 'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll']},
            {'name': 'forms',
             'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                       'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',

            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        # 'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join(
            [
                # your extra plugins here
                'div',
                'autolink',
                'autoembed',
                'embedsemantic',
                'autogrow',
                # 'devtools',
                'widget',
                'lineutils',
                'clipboard',
                'dialog',
                'dialogui',
                'elementspath'
            ]),
    }
}

ADMIN_TOOLS_THEMING_CSS = 'foundation/css/foundation.min.css'


AXES_COOLOFF_TIME = 1
AXES_LOCKOUT_TEMPLATE = None
AXES_LOCKOUT_URL = "https//:www.google.com/"
AXES_DISABLE_SUCCESS_ACCESS_LOG = False
AXES_USERNAME_FORM_FIELD = "username"

"""
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
    ]
}
"""

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAdminUser',

    ],
    'PAGE_SIZE': 10
}

#track settings
TRACK_AJAX_REQUESTS = True
TRACK_ANONYMOUS_USERS = True
TRACK_PAGEVIEWS = True
TRACK_REFERER = True
TRACK_QUERY_STRING = True
