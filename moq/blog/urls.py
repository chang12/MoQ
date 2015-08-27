from django.conf.urls import url


urlpatterns = [
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^(?P<pk>\d+)/$', 'blog.views.group_detail', name='group_detail'),
    url(r'^new$', 'blog.views.group_new', name='group_new'),
    url(r'^edit/(?P<pk>\d+)/$', 'blog.views.group_edit', name='group_edit'),
    url(r'^delete/(?P<pk>\d+)/$', 'blog.views.group_delete', name='group_delete'),
    url(r'^(?P<group_pk>\d+)/(?P<question_pk>\d+)/$', 'blog.views.question_detail', name='question_detail'),
    url(r'^(?P<group_pk>\d+)/new', 'blog.views.question_new', name='question_new'),
    url(r'^(?P<group_pk>\d+)/(?P<question_pk>\d+)/edit/$', 'blog.views.question_edit', name='question_edit'),
    url(r'^(?P<group_pk>\d+)/(?P<question_pk>\d+)/delete/$', 'blog.views.question_delete', name='question_delete')
]
