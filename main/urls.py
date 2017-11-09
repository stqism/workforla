from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^whyla?$', views.whyla, name='whyla'),
    url(r'^aboutus?$', views.aboutus, name='aboutus'),
    url(r'^process?$', views.process, name='process'),
]
