from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('discover.html', views.discover, name='discover'),
    url('collection.html', views.collection, name='collection'),

]
