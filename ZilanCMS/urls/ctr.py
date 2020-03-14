from django.urls import path, include
from ZilanCMS.views import ctr
from ZilanCMS import  serializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register(r'users', serializers.AllUserViewSet)
router.register(r'work', serializers.UploadWorkViewSet)
router.register(r'filetype', serializers.FileTypeViewSet)
# 后台路由
urlpatterns = [
    # rest_framwork
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # admin 后台系统
    path('', ctr.Index.as_view()),  # 正常显示
    path('login/', ctr.Login.as_view()),  # 登录
    path('logout/', ctr.Logout.as_view()),  # 用户登出
    #
    path('user/',ctr.User.as_view()), #用户操作
    path('user/type/', ctr.User.as_view()),  # 用户操作
    path('user/type/<int:pk>/', ctr.TypeUser.as_view()),  # 用户操作
    # path('user1/',ctr.apiuser1), #用户操作
    path('adduser/',ctr.UserAdd.as_view()), #用户操作
    path('edituser/<int:pk>/',ctr.UserEdit.as_view()), #用户操作
    # path('edituser/<int:pk>/',ctr.useredit), #用户操作

    #view 通用操作
    path('home/<slug:mk>/',ctr.Home.as_view()), #用户操作
    path('home/<slug:mk>/type/', ctr.Home.as_view()),  # 用户操作
    path('type/<slug:mk>/', ctr.Home.as_view()),  # 用户操作
    path('type/<slug:mk>/<int:tk>/', ctr.TypeHome.as_view()),  # 用户操作
    # path('home/<slug:mk>/type/<int:pk>/', ctr.TypeBaseHome.as_view()),  # 用户操作
    path('add/<slug:mk>/', ctr.HomeAdd.as_view()),  # 用户操作
    path('edit/<slug:mk>/<int:pk>/', ctr.HomeEdit.as_view()),  # 用户操作
    #

    path('article/', ctr.Article.as_view()),  # 用户操作
    path('article/<int:pk>/', ctr.TypeArticle.as_view()),  # 用户操作
    # path('user1/',ctr.apiuser1), #用户操作
    path('addarticle/', ctr.ArticleAdd.as_view()),  # 用户操作
    path('editarticle/<int:pk>/', ctr.ArticleEdit.as_view()),  # 用户操作

    #


    # path('reg/', ctr.myRegister),

]
# urlpatterns = format_suffix_patterns(urlpatterns)