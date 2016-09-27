from django.conf.urls import url, include
from sitepages import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url('^contact/', views.contact_page, name='contact'),
    url('^about/', views.about_me, name='about'),
    url('^skills/', views.skills, name='skills'),
    url('^article/', views.article, name='article'),
    url('^portfolio/', views.portfolio, name='portfolio'),

]
