from django.conf.urls import url


urlpatterns = [
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^list/$', 'blog.views.group_list', name='group_list'),
    url(r'^(?P<group_pk>\d+)/$', 'blog.views.group_detail', name='group_detail'),
    url(r'^new$', 'blog.views.group_new', name='group_new'),
    url(r'^(?P<group_pk>\d+)/edit/$', 'blog.views.group_edit', name='group_edit'),
    url(r'^(?P<group_pk>\d+)/delete/$', 'blog.views.group_delete', name='group_delete'),
    url(r'^(?P<group_pk>\d+)/like/$', 'blog.views.group_like', name='group_like'),
    url(r'^(?P<group_pk>\d+)/unlike/$', 'blog.views.group_unlike', name='group_unlike'),
    url(r'^(?P<group_pk>\d+)/(?P<question_pk>\d+)/$', 'blog.views.question_detail', name='question_detail'),
    url(r'^(?P<group_pk>\d+)/new', 'blog.views.question_new', name='question_new'),
    url(r'^(?P<group_pk>\d+)/(?P<question_pk>\d+)/edit/$', 'blog.views.question_edit', name='question_edit'),
    url(r'^(?P<group_pk>\d+)/(?P<question_pk>\d+)/delete/$', 'blog.views.question_delete', name='question_delete'),
    url(r'^(?P<group_pk>\d+)/(?P<question_pk>\d+)/like/$', 'blog.views.question_like', name='question_like'),
    url(r'^(?P<group_pk>\d+)/(?P<question_pk>\d+)/unlike/$', 'blog.views.question_unlike', name='question_unlike'),
    url(r'^(?P<group_pk>\d+)/(?P<question_pk>\d+)/new/$', 'blog.views.answer_new', name='answer_new'),
    # url(r'^(?P<group_pk>\d+)/(?P<question_pk>\d+)/(?P<answer_pk>\d+)/$', 'blog.views.answer_detail', name='answer_detail'),
    url(r'^(?P<group_pk>\d+)/(?P<question_pk>\d+)/(?P<answer_pk>\d+)/edit/$', 'blog.views.answer_edit', name='answer_edit'),
    url(r'^(?P<group_pk>\d+)/(?P<question_pk>\d+)/(?P<answer_pk>\d+)/delete/$', 'blog.views.answer_delete', name='answer_delete'),
    url(r'^(?P<group_pk>\d+)/(?P<question_pk>\d+)/(?P<answer_pk>\d+)/like/$', 'blog.views.answer_like', name='answer_like'),
    url(r'^(?P<group_pk>\d+)/(?P<question_pk>\d+)/(?P<answer_pk>\d+)/unlike/$', 'blog.views.answer_unlike', name='answer_unlike'),

    url(r'^practice/$', 'blog.views.practice', name='practice')
]
