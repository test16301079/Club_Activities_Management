"""Club_Activity_Management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.urls import path
from account_app import views
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^upload',views.upload),
    url(r'admin/', admin.site.urls),
    url(r'^login$', views.login, name='login'),
    url(r'^camera$', views.camera, name='camera'),
    url(r'^xiugai$', views.xiugai, name='xiugai'),
    url(r'^loginFaceCheck$', views.loginFaceCheck, name='loginFaceCheck'),
    url(r'^guanli$', views.guanli, name='guanli'),
    url(r'^register$', views.register, name='register'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^$', views.home, name='home'),
    url(r'^manage$', views.manage, name='manage'),
    # url(r'^myContract$', views.myContract, name='myContract'),
    # url(r'^myManageContract$', views.myManageContract, name='myManageContract'),
    # url(r'^setContract$', views.setContract, name='setContract'),
    # url(r'^allContract$', views.allContract, name='allContract'),
    url(r'^xiugai$', views.xiugai, name='xiugai'),
    # url(r'^user$', views.user, name='user'),
    url(r'^Employee', views.Employee, name='Employee'),
    url(r'^allField$', views.allField, name='allField'),
    url(r'^log$', views.log, name='log'),
    url(r'^downloadFile$', views.downloadFile, name='downloadFile'),
    url(r'^news$', views.news, name='news'),
    url(r'^myActivity$', views.myActivity, name='myActivity'),
    url(r'^allActivity$', views.allActivity, name='allActivity'),

    url(r'^testwebscoket/', views.testwebsocket,name='testwebscoket'),
    url(r'^pathweb/', views.pathweb,name='pathweb'),
    url(r'^datasetlink$', views.datasetlink, name='datasetlink'),
    url(r'^datasetlink_old$', views.datasetlink_old, name='datasetlink_old'),
    url(r'^datasetlink_vol$', views.datasetlink_vol, name='datasetlink_vol'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)