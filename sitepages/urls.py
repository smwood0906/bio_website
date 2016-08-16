from django.conf.urls import url
from sitepages import views

urlpatterns = [
    # url(r'^', views.home, name='home'),
    url('^contact/', views.contact_page, name='contact'),
    # url('^about/', views.about_me, name='about'),
]