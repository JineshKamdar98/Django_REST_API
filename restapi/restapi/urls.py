"""restapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin

from updates.views import json_example_view,JsonCBV,JsonCBV2, SerializedListView, SerializedDetailView

from rest_framework_jwt.views import obtain_jwt_token #for crating token
from rest_framework_jwt.views import refresh_jwt_token #for refreshing our token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^json/cbv/$', JsonCBV.as_view()),
    url(r'^json/cbv2/$', JsonCBV2.as_view()),
    url(r'^json/example/$', json_example_view),
    url(r'^json/serializedlist/$', SerializedListView.as_view()),
    url(r'^json/serializeddetail/$', SerializedDetailView.as_view()),
    url(r'^api/updates/', include('updates.api.urls')),
    url(r'^api/status/', include('status.api.urls', namespace='api-status')),
    url(r'^api/auth/', include('accounts.api.urls', namespace='api-auth')), #for accounts app urls.py
    # url(r'^api/auth/jwt/$', obtain_jwt_token),
    # url(r'^api/auth/jwt/refresh/$', refresh_jwt_token),
    #url(r'^api/user/', include('accounts.api.urls_user', namespace='api-user')), #for accounts/api/urls_user.py file
    url(r'^api/user/', include('accounts.api.user.urls', namespace='api-user')), #for accoutns/api/user/urls.py file

]
