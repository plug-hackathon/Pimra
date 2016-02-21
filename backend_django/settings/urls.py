"""settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from pimra import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.IndexTemplateView.as_view()),
    url(r'^nfc/view_dump_nfc', views.view_dump_nfc),
    url(r'^nfc/view_dump_mfoc', views.view_dump_mfoc),
    url(r'^nfc/view_nfc_poll', views.view_nfc_poll),
    url(r'^nfc/view_nfc_write', views.view_nfc_write),

]
