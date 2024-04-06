[![PyPI](https://img.shields.io/pypi/v/django-intra)](https://pypi.org/project/django-intra/)
[![Pylint](https://github.com/ahmdhjj/django-intra/actions/workflows/pylint.yml/badge.svg)](https://github.com/ahmdhjj/django-intra/actions/workflows/pylint.yml)
[![Django CI](https://github.com/ahmdhjj/django-intra/actions/workflows/test.yml/badge.svg)](https://github.com/ahmdhjj/django-intra/actions/workflows/test.yml)
[![Upload Python Package](https://github.com/ahmdhjj/django-intra/actions/workflows/release.yml/badge.svg)](https://github.com/ahmdhjj/django-intra/actions/workflows/release.yml)
# django-intra
## Docs
https://ahmdhjj.github.io/django-intra/

## Installation
```
pip install django-intra
```
## Settings
In your settings file:

1. Add `'intra'` to `INSTALLED_APPS`.

2. Add `'intra/templates'` to the `DIRS` option in the `TEMPLATES` setting:
```
  TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['intra/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
## URL configuration
```
from django.urls import path, include

urlpatterns = [
    ...
    path('admin/', include('intra.urls')),
    ...
]
```
Make sure to remove the default `AdminSite` instance `django.contrib.admin.site` at the URL `/admin/`, i.e. remove the line below:
```
  path('admin/', admin.site.urls),`
```
