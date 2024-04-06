# Welcome to django-intra Docs

## Installation

* `pip install django-intra`

## Settings
In your settings file:
1. Add `'intra'` to `INSTALLED_APPS`.
3. Add `'intra/templates'` to the `DIRS` option in the `TEMPLATES` setting.
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
