
from django.conf.urls import url, include
from django.contrib import admin
from messenger.models import Message
from messenger.views import IndexView, MessageCreateView, UserCreateView, MessageDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^user/new/$', UserCreateView.as_view(), name="user_create_view"),
    url(r'^message/new/$', MessageCreateView.as_view(), name="message_create_view"),
    url(r'^message/(?P<pk>\d+)/$', MessageDetailView.as_view(), name="message_detail_view"),
]
