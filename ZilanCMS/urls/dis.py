from django.urls import path,include
from ZilanCMS import views,serializers
from ZilanCMS.views import dis
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


# 前台显示系统
urlpatterns = [

    # path('', views.index),  # 定义启示
    path('dis/', dis.index),  # 正常显示
    path('login/', dis.Login.as_view()),  # 登录

    path('logout/', dis.myLogout),
    path('reg/', dis.myRegister),
    # 作品保存
    path('uploadwork/', dis.uploadfile, name = 'upload_already_work'),


    #外部请求接口
    path('apilogin/', dis.apiLogin),  # 外界登录登录
    path('apiwork/', dis.apiWorkPost),  # 外部请求work接口


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   #增加开发模式下media文件的访问