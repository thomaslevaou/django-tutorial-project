"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # A partir de l'include ci-dessous, toute URL présente dans polls/urls sera en gros automatiquement ajoutée au urls.py racine
    # Et c'est valable pour n'importe quelle URL dont le path contient "polls/urls" (dont "fun_polls/urls" ou "content/polls/urls" par exemple)
    path('polls/', include('polls.urls')),
    # admin.site.urls est la seule URL n'ayant pas besoin d'include
    path('admin/', admin.site.urls),
]
