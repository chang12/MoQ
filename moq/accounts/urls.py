from django.conf.urls import url


urlpatterns = [
    url(r'^login/$', 'accounts.views.login'),
    url(r'^signup/$', 'accounts.views.signup', name='signup'),
    url(r'^profile/$', 'accounts.views.profile', name='profile'),
]
