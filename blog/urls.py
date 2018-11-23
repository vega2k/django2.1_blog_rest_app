from django.conf.urls import url
from django.urls import include
from rest_framework import routers

from . import viewsets
from . import views

router = routers.DefaultRouter()
router.register(r'posts', viewsets.PostViewSet)


urlpatterns = [
    url(r'^$',views.post_list,name='post_list'),
    url(r'^post/(?P<pk>\d+)/$',views.post_detail,name='post_detail'),
    #url(r'^post/new$',views.post_new,name='post_new')
    url(r'^post/new$', views.post_new_modelform, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]