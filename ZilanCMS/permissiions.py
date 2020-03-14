from rest_framework import permissions
from django.shortcuts import redirect
from django.contrib.auth import logout
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the user of the work.
        return obj.user == request.user

class IsManagerOrReadModifyOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET','PUT','PATCH','HEAD', 'OPTIONS']:
            return True
        if request.user.is_disuser == False :
            return True
        return False
class NoDelateManager(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method not in ['DELETE']:
            return True
        if obj.is_disuser == True:
            return True
        return False

class NoDelate(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ['DELETE']:
            return False
        return True

class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_manager == True:
            return True
        message = "权限错误，请先登录管理员账户"
        logout(request)
        # return redirect('/ctr/login/', locals())
        return False