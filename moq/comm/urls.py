from django.conf.urls import url


urlpatterns = [
    url(r'^$', 'comm.views.index', name='index'),
]
