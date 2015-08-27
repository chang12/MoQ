from django.conf.urls import url


urlpatterns = [
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^(?P<pk>\d+)/$', 'blog.views.group_detail', name='group_detail'),
    url(r'^new$', 'blog.views.group_new', name='group_new'),
    url(r'^edit/(?P<pk>\d+)/$', 'blog.views.group_edit', name='group_edit'),
    url(r'^delete/(?P<pk>\d+)/$', 'blog.views.group_delete', name='group_delete'),
]
