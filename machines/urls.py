from django.conf.urls import url

from . import views

app_name='machines'
urlpatterns = [
    # ex: /machines/
    url(r'^$', views.index, name='index'),
    # ex: /machines/signin/
    url(r'^signin/$', views.signin, name='signin'),
    # ex: /machines/signup/
    url(r'^signup/$', views.signup, name='signup'),
    # ex: /machines/setup/
    url(r'^setup/$', views.setup, name='setup'),
    # ex: /machines/progress/
    url(r'^progress/$', views.progress, name='progress'),
]
