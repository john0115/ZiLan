from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout,models
from django.http import HttpResponse,HttpResponseRedirect,Http404,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

import json
from ZilanCMS import models as mymodels
from ZilanCMS import form as myform
from ZilanCMS.serializers import AllUserSerializer

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from ZilanCMS.permissiions import IsManager
from rest_framework.views import APIView
from rest_framework import status,generics,permissions
from rest_framework.decorators import api_view
def isManagerOrLogin(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_manager == True:
            ret = func(request,*args, **kwargs)
            return ret
        else:
            message = '请先登录再继续操作'
            return redirect('/ctr/login',locals())
    return wrapper
def onlyAllowAdminAndManagerToUserJson(func):
    def wrapper(request, *args, **kwargs):
        pk = request.POST['id']#REST_FRAMOWORK 中request获取数据方式不同
        objectuser = mymodels.AllUser.objects.get(id = pk)
        if request.user.is_admin and objectuser.is_admin == False:
            ret = func(request,*args, **kwargs)
            return ret
        if request.user.is_manager and objectuser.is_manager ==False:
            ret = func(request,*args, **kwargs)
            return ret
        else:
            return JsonResponse({'success': True, 'message': '权限不足'})


    return wrapper
def allowAdminRejectManagerToOtherManager(func):
    def wrapper(request,pk, *args, **kwargs):
        objectuser = mymodels.AllUser.objects.get(id=pk)
        if request.user.is_admin:
            ret = func(request,pk,*args, **kwargs)
            return ret
        if request.user !=objectuser and objectuser.is_manager == True:
            return redirect('/ctr/user')
        ret = func(request,pk,*args, **kwargs)
        return ret

    return wrapper
def allowAdminRejectManagerToOtherManagerInHome(func):
    def wrapper(request,mk, pk, *args, **kwargs):
        if mk=='user':
            objectuser = mymodels.AllUser.objects.get(id=pk)
            if request.user.is_admin:
                ret = func(request,mk, pk,*args, **kwargs)
                return ret
            if request.user !=objectuser and objectuser.is_manager == True:
                return redirect('/ctr/user')
        ret = func(request,mk,pk,*args, **kwargs)
        return ret

    return wrapper

def isHasClass(func):
    def wrapper(request,mk, *args, **kwargs):
        if mk in mk_to_class:
            ret = func(request, mk, *args, **kwargs)
            return ret
        else:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
        return ret

    return wrapper

@method_decorator(isManagerOrLogin,name='dispatch')
class Index(APIView):
    def get(self, request,):
        user = request.user
        return render(request, 'ctr_index.html', locals())

class Login(APIView):
    # authentication_classes = [BasicAuthentication, SessionAuthentication]

    def get(self, request, format=None):
        title = '用户登录'
        if request.user.is_authenticated and request.user.is_manager == True:
            return redirect("/ctr/")
        return render(request, 'ctr_login.html',locals())

    def post(self, request, format=None):
        title = '用户登录'
        message = {}
        una = request.POST.get('id_username')
        psd = request.POST.get('id_password')
        is_ajax = request.POST.get('ajax_status')
        cach_user = authenticate(username=una, password=psd)
        if cach_user is not None and cach_user.is_manager == True and cach_user.is_deleted == False:
            login(request, cach_user)
            message['message'] = '验证成功'
            message['success'] = True
            message['uid'] = cach_user.id
            message['nickname'] = cach_user.nickname
            message['shot'] = cach_user.shot
            message['is_expand'] = cach_user.is_expand
            message['is_pay'] = cach_user.is_pay
        else:
            message['message'] = '验证失败,请重新输入用户名密码'
            message['success'] = False
            message['uid'] = None
            message['nickname'] = None
            message['shot'] = None
            message['is_expand'] = None
            message['is_pay'] = None

        if (message['success']):
             # return render(request, 'dis_index.html', locals())
            return HttpResponseRedirect('/ctr/')
        else:
            return render(request, 'ctr_login.html', message)

    def delete(self, request, pk, format=None):
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

@method_decorator(isManagerOrLogin,name='dispatch')
class Logout(APIView):
    def get(self, request, format=None):
        logout(request)
        return redirect("/ctr/login/")

@method_decorator(isManagerOrLogin,name='get')
@method_decorator(onlyAllowAdminAndManagerToUserJson,name='delete')
class User(APIView):

    def get(self, request, format=None):
        title = '用户管理'
        user = request.user
        types = {}

        if(user.is_admin):####权限问题
            manager = mymodels.AllUser.objects.filter(is_manager=True, is_admin=False,is_deleted=False)
        else:
            manager = mymodels.AllUser.objects.filter(is_manager=False , is_admin=False, is_deleted=False)
            types = mymodels.UserType.objects.all()
        manager_serial = AllUserSerializer(manager,many=True)
        datas =manager_serial.data
        action = '/ctr/user/'
        type_action ='/ctr/user/type/'
        return render(request, 'ctr_user.html', locals())

    def delete(self, request, format=None):
        '''
        user delete 函数
        :param request:
        :param format:
        :return:message 提示信息
         '''
        pk = request.POST['id']
        objectuser = mymodels.AllUser.objects.get(id = pk)
        if objectuser is not None:
            objectuser.is_deleted = True
            objectuser.save()
            return JsonResponse({'success':True,'message':'管理员删除成功'})
            # return redirect('/ctr/user/')
        else:
            # return render(request, 'ctr_user.html', data)
            return JsonResponse({'success':False,'message':'用户不存在'})

    def post(self, request, format=None):
        return self.delete(request, format)
@method_decorator(isManagerOrLogin,name='get')
class TypeUser(APIView):
    def get(self, request, pk=1, format=None):
        title = '用户管理'
        user = request.user
        usertype = mymodels.UserType.objects.filter(id = pk)
        types = {}
        if len(usertype) == 0 :
            message = '用户类型选择错误'
        else:
            if (user.is_admin):  ####权限问题
                manager = mymodels.AllUser.objects.filter(is_manager=True, is_admin=False, is_deleted=False)
            else:
                manager = mymodels.AllUser.objects.filter(is_manager=False, is_admin=False, is_deleted=False, type=usertype[0])
                types = mymodels.UserType.objects.all()
            manager_serial = AllUserSerializer(manager, many=True)
            datas = manager_serial.data
        action = '/ctr/user/'
        type_action = '/ctr/user/type/'
        return render(request, 'ctr_user.html', locals())

@method_decorator(isManagerOrLogin,name='dispatch')
@method_decorator(allowAdminRejectManagerToOtherManager,name='dispatch')
class UserEdit(APIView):

    def get(self, request, pk , format=None):
        title = '用户编辑'
        action= '/ctr/edituser/'+str(pk)+'/'
        method = 'POST'
        objectuser = mymodels.AllUser.objects.get(id=pk)
        objectuser.password = ''
        form = myform.user_form(instance=objectuser)
        return render(request, 'ctr_adduser.html', locals())
    def post(self, request,pk, format=None):
        title = '用户编辑'
        action = '/ctr/edituser/' + str(pk) + '/'
        method = 'POST'
        objectuser = mymodels.AllUser.objects.get(id=pk)
        form = myform.user_form(request.POST,instance=objectuser)
        password = request.POST['password']
        if form.is_valid():
            form.save()
            if (password):
                objectuser.set_password(password)  ##设置密码  save之后才有效
                objectuser.save()
            message = '数据保存成功'
            return render(request, 'ctr_adduser.html', locals())
        else:
            message = '数据校验失败'
            return render(request, 'ctr_adduser.html', locals())

@method_decorator(isManagerOrLogin,name='dispatch')
class UserAdd(APIView):
    def get(self, request, format=None):
        user = request.user
        title = '用户增加'
        form = myform.user_form()
        action = '/ctr/adduser/'
        method = 'post'
        return render(request,'ctr_adduser.html',locals())
    def post(self, request, format=None):
        title = '用户增加'
        form = myform.user_form(request.POST)
        if form.is_valid():
            user = mymodels.AllUser.objects.create_user(username=form.cleaned_data['username'],
                                               email=form.cleaned_data['email'],
                                               phone=form.cleaned_data['phone'],
                                               password=form.cleaned_data['password'],
                                               is_manager=True,
                                               is_disuser=False)

            message = '保存成功'
            form = myform.user_form()
            action = '/ctr/adduser/'
            method = 'post'
            return render(request, 'ctr_adduser.html', locals())
        else:
            message = '数据校验错误'
            action = '/ctr/adduser/'
            method = 'post'
            return render(request, 'ctr_adduser.html', locals())

mk_to_class = {'user':'AllUser', 'usertype':'UserType', 'article':'BaseArticle', 'articletype':'ArticleType'}
mk_to_typeclass = {'user':'UserType', 'article':'ArticleType'}
fields = {'user':{'username':'用户姓名','phone':'电话号码'},
          'usertype':{'typename':'类型名称'},
          'article': {'title':'文章标题','update_time':'发布时间','user':'发布人'},
          'articletype': {'typename':'类型名称'},}
titles = {'user':'用户管理', 'usertype':'用户类型管理', 'article':'文章管理', 'articletype':'文章类型管理'}
mk_to_form = {'user':'user_form()', 'usertype':'usertype_form', 'article':'article_form', 'articletype':'atricletype_form'}

@method_decorator(isManagerOrLogin,name='get')
@method_decorator(isHasClass,name='dispatch')
class Home(APIView):
    def get(self, request, mk, format=None):
        user = request.user
        title = titles[mk]
        target_model = eval('mymodels.'+mk_to_class[mk])
        if mk in mk_to_typeclass:
            type_model = eval('mymodels.' + mk_to_typeclass[mk])
            alltypes = type_model.objects.filter(is_deleted=False)
        if (mk == 'user'):
            if (user.is_admin):  ####权限问题
                datas = mymodels.AllUser.objects.filter(is_manager=True, is_admin=False, is_deleted=False)
            else:
                datas = mymodels.AllUser.objects.filter(is_manager=False, is_admin=False, is_deleted=False,)
        else:
            datas =target_model.objects.filter(is_deleted=False)
        action = '/ctr/home/'+mk+'/'
        field = fields[mk]
        return render(request, 'ctr_home.html', locals())

    def delete(self, request, mk, format=None):
        '''
        user delete 函数
        :param request:
        :param format:
        :return:message 提示信息
         '''
        pk = request.POST['id']
        target_model = eval('mymodels.' + mk_to_class[mk])
        target = target_model.objects.get(id = pk)
        if target is not None:
            if mk in mk_to_typeclass:  #重要类型数据删除为设置is_deleted，方便恢复
                target.is_deleted = True
                target.save()
            else:#直接删除
                target.delete()
            return JsonResponse({'success':True,'message':'删除成功'})
        else:
            return JsonResponse({'success':False,'message':'类型不存在'})

    def post(self, request, mk, format=None):
        return self.delete(request,mk, format)

@method_decorator(isManagerOrLogin,name='get')
class TypeHome(APIView):
    def get(self, request, mk, tk =1, format=None):
        user = request.user
        title = titles[mk]
        target_model = eval('mymodels.'+mk_to_class[mk])
        type_model = eval('mymodels.' + mk_to_typeclass[mk])
        type = type_model.objects.filter(id = tk)
        alltypes = type_model.objects.filter(is_deleted=False)

        # action = '/ctr/home/' + mk + '/'
        # type_action = '/ctr/type/' + mk + '/'
        field = fields[mk]
        if len(type) == 0 :
            message = '用户类型选择错误'
        else:
            if(mk == 'user'):
                if (user.is_admin):  ####权限问题
                    datas = mymodels.AllUser.objects.filter(is_manager=True, is_admin=False, is_deleted=False)
                else:
                    datas = mymodels.AllUser.objects.filter(is_manager=False, is_admin=False, is_deleted=False, type=type[0])
            else:
                datas = target_model.objects.filter(is_deleted=False, type=type[0])

        return render(request, 'ctr_home.html', locals())

@method_decorator(isManagerOrLogin,name='dispatch')
@method_decorator(allowAdminRejectManagerToOtherManagerInHome,name='dispatch')
@method_decorator(isHasClass,name='dispatch')
class HomeEdit(APIView):

    def get(self, request,mk, pk , format=None):
        title = titles[mk]
        action = '/ctr/edit/' + mk + '/' + str(pk) + '/'
        method = 'POST'
        target_model = eval('mymodels.' + mk_to_class[mk])
        object = target_model.objects.get(id=pk)
        object.password = ''
        form = eval('myform.' + mk + '_form(instance=object)')
        return render(request, 'ctr_addhome.html', locals())
    def post(self, request, mk, pk, format=None):
        title = titles[mk]
        action = '/ctr/edit/'+mk+'/'+str(pk)+'/'
        method = 'POST'
        target_model = eval('mymodels.' + mk_to_class[mk])
        object = target_model.objects.get(id=pk)
        form = eval('myform.' + mk + '_form(request.POST,instance=object)')
        password = ''
        if 'password' in request.POST:
            password = request.POST['password']
        if form.is_valid():
            form.save()
            if (password):
                object.set_password(password)  ##设置密码  save之后才有效
                object.save()
            message = '数据保存成功'
            return render(request, 'ctr_addhome.html', locals())
        else:
            message = '数据校验失败'
            return render(request, 'ctr_addhome.html', locals())

@method_decorator(isManagerOrLogin,name='dispatch')
@method_decorator(isHasClass,name='dispatch')
class HomeAdd(APIView):
    def get(self, request, mk,  format=None):
        user = request.user
        title = titles[mk]
        form = eval('myform.'+mk+'_form()')
        action = '/ctr/add/'+mk+'/'
        method = 'post'
        return render(request,'ctr_addhome.html',locals())
    def post(self, request, mk, format=None):
        title = titles[mk]
        form = eval('myform.' + mk + '_form(request.POST)')
        if form.is_valid():
            # user = mymodels.AllUser.objects.create_user(username=form.cleaned_data['username'],
            #                                    email=form.cleaned_data['email'],
            #                                    phone=form.cleaned_data['phone'],
            #                                    password=form.cleaned_data['password'],
            #                                    is_manager=True,
            #                                    is_disuser=False)
            object = form.save(commit = False)
            if mk == 'user':
                object.set_password(form.cleaned_data['password'])
                if request.user.is_admin:# admin添加管理用户 manger 添加前端用户
                    object.is_manager = True
                    object.is_disuser = False
                else:
                    object.is_manager = False
                    object.is_disuser = True
            if mk == 'article':
                object.user = request.user
            object.save()

            message = '保存成功'
            form = eval('myform.' + mk + '_form()')
            action = '/ctr/add/' + mk + '/'
            method = 'post'
            return render(request, 'ctr_addhome.html', locals())
        else:
            message = '数据校验错误'
            action = '/ctr/add/' + mk + '/'
            method = 'post'
            return render(request, 'ctr_addhome.html', locals())

####文章类控制器
@method_decorator(isManagerOrLogin,name='get')
@method_decorator(onlyAllowAdminAndManagerToUserJson,name='delete')
class Article(APIView):

    def get(self, request, format=None):
        title = '用户管理'
        user = request.user
        types = {}
        if(user.is_admin):####权限问题
            manager = mymodels.AllUser.objects.filter(is_manager=True, is_admin=False,is_deleted=False)
        else:
            manager = mymodels.AllUser.objects.filter(is_manager=False , is_admin=False, is_deleted=False)
            types = mymodels.UserType.objects.all()
        manager_serial = AllUserSerializer(manager,many=True)
        datas =manager_serial.data
        action = '/ctr/user/'
        return render(request, 'ctr_user.html', locals())

    def delete(self, request, format=None):
        '''
        user delete 函数
        :param request:
        :param format:
        :return:message 提示信息
         '''
        pk = request.POST['id']
        objectuser = mymodels.AllUser.objects.get(id = pk)
        if objectuser is not None:
            objectuser.is_deleted = True
            objectuser.save()
            return JsonResponse({'success':True,'message':'管理员删除成功'})
            # return redirect('/ctr/user/')
        else:
            # return render(request, 'ctr_user.html', data)
            return JsonResponse({'success':False,'message':'用户不存在'})

    def post(self, request, format=None):
        return self.delete(request, format)
@method_decorator(isManagerOrLogin,name='get')
class TypeArticle(APIView):
    def get(self, request, pk=1, format=None):
        title = '用户管理'
        user = request.user
        usertype = UserType.objects.filter(id = pk)
        types = {}
        if len(usertype) == 0 :
            message = '用户类型选择错误'
        else:
            if (user.is_admin):  ####权限问题
                manager = mymodels.AllUser.objects.filter(is_manager=True, is_admin=False, is_deleted=False)
            else:
                manager = mymodels.AllUser.objects.filter(is_manager=False, is_admin=False, is_deleted=False, type=usertype[0])
                types = UserType.objects.all()
            manager_serial = AllUserSerializer(manager, many=True)
            datas = manager_serial.data
        action = '/ctr/user/'
        return render(request, 'ctr_user.html', locals())

@method_decorator(isManagerOrLogin,name='dispatch')
@method_decorator(allowAdminRejectManagerToOtherManager,name='dispatch')
class ArticleEdit(APIView):

    def get(self, request, pk , format=None):
        title = '用户编辑'
        action= '/ctr/edituser/'+str(pk)+'/'
        method = 'POST'
        objectuser = mymodels.AllUser.objects.get(id=pk)
        objectuser.password = ''
        form = myform.user_form(instance=objectuser)
        return render(request, 'ctr_adduser.html', locals())
    def post(self, request,pk, format=None):
        title = '用户编辑'
        action = '/ctr/edituser/' + str(pk) + '/'
        method = 'POST'
        objectuser = mymodels.AllUser.objects.get(id=pk)
        form = myform.user_form(request.POST,instance=objectuser)
        password = request.POST['password']
        if form.is_valid():
            form.save()
            if (password):
                objectuser.set_password(password)  ##设置密码  save之后才有效
                objectuser.save()
            message = '数据保存成功'
            return render(request, 'ctr_adduser.html', locals())
        else:
            message = '数据校验失败'
            return render(request, 'ctr_adduser.html', locals())

@method_decorator(isManagerOrLogin,name='dispatch')
class ArticleAdd(APIView):
    def get(self, request, format=None):
        user = request.user
        title = '用户增加'
        form = myform.user_form()
        action = '/ctr/adduser/'
        method = 'post'
        return render(request,'ctr_adduser.html',locals())
    def post(self, request, format=None):
        title = '用户增加'
        form = myform.user_form(request.POST)
        if form.is_valid():
            user = mymodels.AllUser.objects.create_user(username=form.cleaned_data['username'],
                                               email=form.cleaned_data['email'],
                                               phone=form.cleaned_data['phone'],
                                               password=form.cleaned_data['password'],
                                               is_manager=True,
                                               is_disuser=False)

            message = '保存成功'
            form = myform.user_form()
            action = '/ctr/adduser/'
            method = 'post'
            return render(request, 'ctr_adduser.html', locals())
        else:
            message = '数据校验错误'
            action = '/ctr/adduser/'
            method = 'post'
            return render(request, 'ctr_adduser.html', locals())




