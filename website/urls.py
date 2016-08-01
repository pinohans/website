"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import website.views as website_views
import django.contrib.auth.views as auth_views
import solvedata.views as data_views

urlpatterns = [
    url(r'^upload/$',data_views.upload),
    url(r'^download/(.+?)/(.+?)/(.+?)/$',data_views.download),
    url(r'^delete/(.+?)/(.+?)/(.+?)/$',data_views.delete),
	url(r'^data/$',data_views.index,name='data_index'),
    url(r'^data/user$',data_views.user,name='data_user'),
    url(r'^data/func2/2$',data_views.func2_2,name='data_func2_2'),
    url(r'^data/func2/result$',data_views.func2_result,name='data_func2_result'),
    url(r'^data/func2/result/view/(.+?)/$',data_views.func2_result_view,name='data_func2_view'),
    url(r'^data/func1/1$',data_views.func1_1,name='data_func1_1'),
    url(r'^data/func1/result$',data_views.func1_result,name='data_func1_result'),
    url(r'^data/func1/result/view/(.+?)/$',data_views.func1_result_view,name='data_func1_view'),
	url(r'^logout/',website_views.logout,name='logout'),
	url(r'^login/',website_views.login,name='login'),
	url(r'^register/',website_views.register,name='register'),
	url(r'^$',website_views.home,name='home'),
    url(r'^admin/', admin.site.urls),
]
