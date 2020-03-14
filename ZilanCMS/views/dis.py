#by John 2020.1.15 前台views
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout,models
from django.http import HttpResponse,HttpResponseRedirect,Http404,JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json
from ZilanCMS.models import AllUser, UploadWork
from ZilanCMS import form
from ZilanCMS.serializers import UploadWorkSerializer,UploadWorkViewSet

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.views import APIView
from rest_framework import status

#专门作为外部api登录接口
@csrf_exempt
def apiLogin(request):
    if  request.user.is_authenticated:
        # return redirect("/dis/")
        return HttpResponse('重复登录')
    message = {}
    # user = AllUser.objects.create_user('admin1', 'admin1@admin.com', 'admin')
    # user.save()
    if request.method == 'POST':
        una = request.POST.get('id_username')
        psd = request.POST.get('id_password')
        is_ajax = request.POST.get('ajax_status')
        cach_user = authenticate(username=una, password=psd)
        if cach_user is not None:
            login(request,cach_user)
            message['mess'] = '验证成功'
            message['success'] = True
            message['uid'] = cach_user.id
            message['nickname'] = cach_user.nickname
            message['shot'] = cach_user.shot
            message['is_expand'] = cach_user.is_expand
            message['is_pay'] = cach_user.is_pay
        else:
            message['mess'] = '验证失败,请重新输入用户名密码'
            message['success'] = False
            message['uid'] = None
            message['nickname'] = None
            message['shot'] = None
            message['is_expand'] = None
            message['is_pay'] = None
        if is_ajax:#ajax提交只返回json数据
            http = HttpResponse(json.dumps(message))
            http['Access-Control-Allow-Origin'] = "*"
            return http
        else:
            if(message['success']):
            # return render(request, 'dis_index.html', locals())
                return HttpResponseRedirect('/dis/')
            else:
                return render(request, 'dis_login.html', message)
    else:
        return HttpResponse('请求方式应为POST')
# rest_framework 自带函数
from rest_framework.renderers import JSONRenderer,HTMLFormRenderer   #json打包
from rest_framework.parsers import JSONParser,FormParser  #解释json
#专门作为外部请求文件接口
@csrf_exempt
def apiWorkPost(request):
    '''
    :param request: ['filename', 'file_illustrate' ,'location', 'thumbnail', 'user'] type：multipart/form-data
    :return: GET ;['filename', 'file_illustrate' ,'location', 'thumbnail', 'user'，]
    POST['filename', 'file_illustrate' ,'location', 'thumbnail', 'user'，]
    ERROR:['error']
    type：json
    '''
    if request.user.is_authenticated:
        if request.method =='GET':
            works = request.user.uploadwork.all()
            workserial = UploadWorkSerializer(works, many=True)
            http = HttpResponse(json.dumps(workserial.data))
        if request.method == 'POST':
            data = FormParser().parse(request)
            fileserial = UploadWorkSerializer(data=data)
            if fileserial.is_valid():
                fileserial.user = request.user
                fileserial.save()
                message = '保存成功'
                http = HttpResponse(JSONRenderer().render(fileserial.data))
            else:
                http =  HttpResponse(JSONRenderer().render(fileserial.errors))
    else:
        http = HttpResponse(json.dumps({'error':'请先登录'}))
    http['Access-Control-Allow-Origin'] = "*"
    return http

def index(request):
    # authentication_classes = (SessionAuthentication, BasicAuthentication)
    if request.user.is_authenticated:
        user = request.user
        works = user.uploadwork.all()
        return render(request, 'dis_index.html', locals())

    else:
        message = {}
        message['mess'] = "请先登录"
        return render(request, 'dis_login.html', message)

class Login(APIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    def  get_object(self, pk):
        try:
            pass
        except AllUser.DoesNotExist:
            raise Http404
    def get(self, request, format=None):
        return render(request, 'dis_login.html')
    def put(self, request, format=None):
        return render(request, 'dis_login.html')
    def post(self, request, format=None):
        message = {}
        una = request.POST.get('id_username')
        psd = request.POST.get('id_password')
        is_ajax = request.POST.get('ajax_status')
        cach_user = authenticate(username=una, password=psd)
        if cach_user is not None and cach_user.is_manager==False and cach_user.is_deleted ==False:
            login(request, cach_user)
            message['mess'] = '验证成功'
            message['success'] = True
            message['uid'] = cach_user.id
            message['nickname'] = cach_user.nickname
            message['shot'] = cach_user.shot
            message['is_expand'] = cach_user.is_expand
            message['is_pay'] = cach_user.is_pay
        else:
            message['mess'] = '验证失败,请重新输入用户名密码'
            message['success'] = False
            message['uid'] = None
            message['nickname'] = None
            message['shot'] = None
            message['is_expand'] = None
            message['is_pay'] = None
        if is_ajax:  # ajax提交只返回json数据
            http = HttpResponse(json.dumps(message))
            http['Access-Control-Allow-Origin'] = "*"
            return http
        else:
            if (message['success']):
                # return render(request, 'dis_index.html', locals())
                return HttpResponseRedirect('/dis/')
            else:
                return render(request, 'dis_login.html', message)

    def delete(self, request, pk, format=None):
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

def myRegister(request):
    if  request.user.is_authenticated:
        return redirect("/dis/")
    if request.method == 'POST':
        user_form = form.user_form(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.is_manger = False
            user.set_password(request.POST.get('password'))
            user.save()
            # user.is_diuser = True
            # user = AllUser.objects.create_user(username=user_form.cleaned_data['username'],
            #                                    email=user_form.cleaned_data['email'],
            #                                    phone=user_form.cleaned_data['phone'],
            #                                    password=user_form.cleaned_data['password'],
            #                                    is_manager=False)
            login(request, user)
            return redirect("/dis/")
        else:
            return render(request, 'dis_register.html', locals())
    else:
        user_form = form.user_form()
        return render(request, 'dis_register.html', locals())
def myLogout(request):
    logout(request)
    return redirect("/login/")
#前端不适用注销功能
# def myLogoff(request):
#     user = request.user
#     user.is_deleted = True
#     user.save()
#     logout(request)
#     return redirect("/login/")
def uploadfile(request):
    # if request.user.is_authenticated:
        user = AllUser.objects.get(username="admin")
        if request.method == 'GET':
            fileform = form.uploadfile_form()
            # files = UploadWorkSerializer.
            return render(request, 'dis_upload_work.html', locals())
        else:
            file = UploadWork.objects.create(user=user)
            fileform = form.uploadfile_form(request.POST or None, request.FILES or None, instance=file)
            if fileform.is_valid():
                # file = fileform.save(commit=False)
                # file.user = user
                # file.save()
                fileform.save()
                message = '上传成功'
                return render(request, 'dis_upload_work.html', locals())
            else:
                message = '数据校验失败'
                return render(request, 'dis_upload_work.html', locals())

    # else:
    #     message = {}
    #     message['mess'] = "请先登录"
    #     return render(request, 'dis_login.html', message)

