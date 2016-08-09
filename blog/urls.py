from django.conf.urls import url, include
from blog import views
from blog.views import EditPost, DeletePost, CreatePost

urlpatterns = [
    url(r'^$', views.blog_list, name='blog_list'),
    url(r'^(?P<cat>[-\w]+)/(?P<slug>[-\w]+)/', include ([
        url(r'^$', views.blog, name='blog'),
        url(r'^edit/$', EditPost.as_view(), name='post_edit'),
        url(r'^delete/$', DeletePost.as_view(), name='post_delete'),
    ])),
url(r'^new/?$', CreatePost.as_view(), name='post_create'),

    url(r'^(?P<cat>[-\w]+)?$', views.cat)
]
