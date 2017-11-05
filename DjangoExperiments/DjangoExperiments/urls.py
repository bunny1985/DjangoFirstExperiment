"""DjangoExperiments URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include 
from django.contrib import admin 
from django.contrib.auth import  views as authViews
from main import views as mainViews
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
import sys;
schema_view = get_swagger_view(title='Pastebin API')

admin.autodiscover()


router = routers.DefaultRouter()
router.register(r'news', mainViews.NewsViewSet)

router.register(r'users', mainViews.UsersViewSet)
router.register(r'groups', mainViews.GroupsViewSet)

apiurls = router.urls
apiurls+= [url(r'news/(?P<pk>.*)/publish', mainViews.publish_news)]
apiurls+= [url(r'news/(?P<pk>.*)/unpublish', mainViews.unpublish_news)]
apiurls+= [url(r'news/latest', mainViews.latestNews)]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', mainViews.hello),
    url(r'^manage$', mainViews.manage , name="manage"),
    url(r'^login$', authViews.login),
    url(r'^logout$', authViews.logout),
    url(r'^403$', authViews.login_required),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^myapi/', include(apiurls)),
    url(r'^swaggerui$', schema_view)
    
    #url(r'^manage/' , include(main ))
]
#urlpatterns += patterns('django.contrib.auth.views')
