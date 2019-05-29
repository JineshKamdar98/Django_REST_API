from django.conf.urls import url
from .views import StatusAPIView, StatusAPIDetailView #StatusDetailAPIView, StatusListAPIView, StatusCreateAPIView, StatusUpdateAPIView, StatusDeleteAPIView

urlpatterns = [
    url(r'^$', StatusAPIView.as_view(), name='list'),
    url(r'^(?P<id>\d+)/$', StatusAPIDetailView.as_view(), name='detail'),  #api/status/12/
    #url(r'^create/$', StatusCreateAPIView.as_view()),
    #url(r'^(?P<pk>\d+)/$', StatusDetailAPIView.as_view()),
    #url(r'^(?P<pk>\d+)/update/$', StatusUpdateAPIView.as_view()),
    #url(r'^(?P<pk>\d+)/delete/$', StatusDeleteAPIView.as_view()),
]
