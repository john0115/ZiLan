"""ZiLan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from ZilanCMS.urls import dis as disurls
from ZilanCMS.urls import ctr as ctrurls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('django-admin/', admin.site.urls),
    #Dis前台路径
    path('', include(disurls)),
    #ctr后台路径
    path('ctr/', include(ctrurls)),

    # path('logout/', admin.site.urls),#登出
    # path('register/', admin.site.urls),#注册
    # path('cancellation/', admin.site.urls),#注销账户



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # 增加开发模式下media文件的访问