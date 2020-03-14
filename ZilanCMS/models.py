from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
import os

class UserType(models.Model):
    """
     用户组别
     """
    typename = models.CharField('类型名称', max_length=100, null=False)
    is_deleted = models.BooleanField('是否已删除', default=False)
    def __str__(self):
        return self.typename
    class Meta:
        managed = True

#全部用户表 修改后 用户认证需要从AllUser表进行认证
class AllUser(AbstractUser):
    """
    用户信息表
    """
    phone = models.CharField('电话', max_length=11, null=False, unique=True, )
    company = models.CharField('单位', max_length=100, null=True, )
    type = models.ForeignKey(UserType, null=False, on_delete=models.CASCADE, verbose_name='组别')
    nickname = models.CharField('昵称', max_length=20, null=True,)
    shot = models.CharField('头像', max_length=300, null=True,)
    is_deleted = models.BooleanField('是否已删除', default=False)
    is_expand = models.BooleanField('是否为扩展账户', default=False)
    is_pay = models.BooleanField('是否为付费账户', default=False)
    is_disuser = models.BooleanField('是否为前台账户', default=True)
    is_manager = models.BooleanField('是否为管理员', default=False)
    is_admin = models.BooleanField('是否为超级管理员',default=False)
    def __str__(self):
        return self.username
    class Meta:
        managed = True

##保存文件相关模型
class FileType(models.Model):
    """
     作品类型
     """
    typename = models.CharField('类型名称', max_length=100, null=False)
    is_deleted = models.BooleanField('是否已删除', default=False)
    def __str__(self):
        return self.typename
    class Meta:
        managed = True

def user_directory_path(instance, filename):
    """
    :param instance: 实例
    :param filename: 文件名
    :return: 带文件名的文件路径
    """
    # ext = filename.split('.')[-1]
    return os.path.join(str(instance.user.id) ,filename)

class UploadWork(models.Model):
    """
    上传的作品
    """
    user = models.ForeignKey('AllUser', related_name='uploadwork', on_delete=models.CASCADE, verbose_name='用户',)
    filename = models.CharField('作品名称', max_length=100, null=False)
    file_illustrate = models.TextField('作品说明',)
    operate_illustrate = models.TextField('操作说明',)
    # location = models.CharField('存储路径', max_length=300, null=False)
    location = models.FileField('文件存储位置', upload_to=user_directory_path, null=False)
    # thumbnail = models.CharField('缩略图片位置', max_length=300, null=False)
    thumbnail = models.ImageField('缩略图片位置', upload_to=user_directory_path, default='common/thumbnail.jpg')
    hittimes = models.IntegerField('点击数', default=0)
    thumbup = models.IntegerField('点赞数', default=0)
    type = models.ForeignKey(FileType, null=True, on_delete=models.CASCADE, verbose_name='类型')
    is_publish = models.BooleanField('是否发布', default=False)
    is_charge = models.BooleanField('是否收费', default=False)
    is_deleted = models.BooleanField('是否已删除', default=False)
    create_time = models.DateTimeField('添加时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    def __str__(self):
        return self.filename
    class Meta:
        managed = True

####网站发布相关模型
class WebSet(models.Model):
    """
    网站基本信息
    """
    user = models.ForeignKey('AllUser', related_name='webset', on_delete=models.CASCADE, verbose_name='用户',)
    name = models.CharField('网站标题', max_length=200, null=False)
    nick_name = models.CharField('网站别名', max_length=200,)
    verify_api = models.CharField('api验证串', max_length=300, )
    extend = models.TextField('扩展说明(百度验证等)', )
    mobile_logo = models.ImageField('手机网站logo', upload_to=user_directory_path, default='common/m_logo.jpg')
    logo = models.ImageField('网站logo', upload_to=user_directory_path, default='common/logo.jpg')
    backstage_logo = models.ImageField('后台logo', upload_to=user_directory_path, default='common/b_logo.jpg')
    backstage_login_logo = models.ImageField('后台登录logo', upload_to=user_directory_path, default='common/l_logo.jpg')
    hittimes = models.IntegerField('阅读量', default=0)
    is_open = models.BooleanField('是否开放', default=False)
    close_note = models.CharField('关闭说明', max_length=200)
    is_deleted = models.BooleanField('是否已删除', default=False)
    tpl_style = models.CharField('模板风格', max_length=200,default='default')
    create_time = models.DateTimeField('添加时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        managed = True

class ArticleType(models.Model):
    """
     网站发布内容类型
     """
    typename = models.CharField('类型名称', max_length=100, null=False)
    tag = models.SlugField('标志字符串', max_length=50, null=False,unique=True)
    num = models.PositiveIntegerField('加载文章数量', default=5)
    is_deleted = models.BooleanField('是否已删除', default=False)
    def __str__(self):
        return self.typename
    class Meta:
        managed = True
class BaseArticle(models.Model):
    """
    基类内容模型
    """
    user = models.ForeignKey('AllUser', related_name='article', on_delete=models.CASCADE, verbose_name='用户',)
    title = models.CharField('文章标题', max_length=200, null=False)
    title2 = models.CharField('文章副标题', max_length=300,)
    link = models.CharField('链接地址', max_length=300, null=True)
    note = models.TextField('文章摘要',)
    content = models.TextField('文章内容',)
    # location = models.CharField('存储路径', max_length=300, null=False)
    enclosure = models.FileField('文件存储位置', upload_to=user_directory_path, null=True)
    # thumbnail = models.CharField('缩略图片位置', max_length=300, null=False)
    thumbnail = models.ImageField('缩略图片位置', upload_to=user_directory_path, default='common/thumbnail.jpg',null=True)
    hittimes = models.IntegerField('阅读量', default=0)
    thumbup = models.IntegerField('点赞数', default=0)
    type = models.ForeignKey('ArticleType', null=True, on_delete=models.CASCADE, verbose_name='文章类型')
    sort = models.PositiveIntegerField('排序', default=0)
    is_publish = models.BooleanField('是否发布', default=True)
    is_hide = models.BooleanField('是否隐藏', default=False)
    is_deleted = models.BooleanField('是否已删除', default=False)
    create_time = models.DateTimeField('添加时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    def __str__(self):
        return self.title
    class Meta:
        managed = True
        ordering = ['-sort']
class Navigation(models.Model):
    """
    导航条
    """
    user = models.ForeignKey('AllUser', related_name='navigation', on_delete=models.CASCADE, verbose_name='用户',)
    title = models.CharField('导航标题', max_length=200, null=False)
    tag = models.CharField('导航标志字符串', max_length=30,)
    url = models.CharField('导航条外部链接', max_length=300,)
    hittimes = models.IntegerField('点击量', default=0)
    article_type = models.ForeignKey(ArticleType, null=True, on_delete=models.CASCADE, verbose_name='加载文章类别')
    article_num = models.PositiveIntegerField('加载文章数量', default=5)
    sort = models.PositiveIntegerField('排序', default=0)
    is_publish = models.BooleanField('是否发布', default=True)
    is_hide = models.BooleanField('是否隐藏', default=False)
    is_deleted = models.BooleanField('是否已删除', default=False)
    create_time = models.DateTimeField('添加时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    def __str__(self):
        return self.title
    class Meta:
        managed = True
        ordering = ['-sort']

class Picture(models.Model):
    """
    基类内容模型
    """
    user = models.ForeignKey('AllUser', related_name='picture', on_delete=models.CASCADE, verbose_name='用户',)
    title = models.CharField('文章标题', max_length=200, null=False)
    link = models.CharField('链接地址', max_length=300, null=True)
    content = models.ImageField('文件存储位置', upload_to=user_directory_path)
    # thumbnail = models.CharField('缩略图片位置', max_length=300, null=False)
    thumbnail = models.ImageField('缩略图片位置', upload_to=user_directory_path, default='common/thumbnail.jpg')
    hittimes = models.IntegerField('阅读量', default=0)
    sort = models.PositiveIntegerField('排序', default=0)
    is_publish = models.BooleanField('是否发布', default=True)
    is_hide = models.BooleanField('是否隐藏', default=False)
    is_deleted = models.BooleanField('是否已删除', default=False)
    create_time = models.DateTimeField('添加时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    def __str__(self):
        return self.title
    class Meta:
        managed = True
        ordering = ['-sort']


class Partner(models.Model):
    """
    基类内容模型
    """
    user = models.ForeignKey('AllUser', related_name='partner', on_delete=models.CASCADE, verbose_name='用户',)
    name = models.CharField('名称', max_length=200, null=False)
    link = models.CharField('链接地址', max_length=300, null=True)
    logo = models.ImageField('logo', upload_to=user_directory_path, default='common/thumbnail.jpg')

    hittimes = models.IntegerField('阅读量', default=0)
    thumbup = models.IntegerField('点赞数', default=0)
    sort = models.PositiveIntegerField('排序', default=0)
    is_publish = models.BooleanField('是否发布', default=True)
    is_hide = models.BooleanField('是否隐藏', default=False)
    is_deleted = models.BooleanField('是否已删除', default=False)
    create_time = models.DateTimeField('添加时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        managed = True
        ordering = ['-sort']


class Stmp(models.Model):
    """
    stmp服务器设置
    """
    user = models.ForeignKey('AllUser', related_name='stmp', on_delete=models.CASCADE, verbose_name='用户', )
    server = models.CharField('名称', max_length=200, null=False)
    port = models.IntegerField('端口', default=25)
    account = models.CharField('账户', max_length=200, null=False)
    password = models.CharField('账户密码', max_length=200, null=False)
    poster = models.CharField('发件人姓名', max_length=200, null=False)
    mail = models.CharField('邮箱地址', max_length=200, null=False)
    encoded = models.CharField('邮件编码', default='UTF-8', max_length=20)

    is_ssl = models.BooleanField('是否启用ssl', default=False)
    is_deleted = models.BooleanField('是否已删除', default=False)
    create_time = models.DateTimeField('添加时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.server

    class Meta:
        managed = True

class Meessage(models.Model):
    """
    留言模型
    """
    user = models.ForeignKey('AllUser', related_name='message', on_delete=models.CASCADE, verbose_name='用户',)
    title = models.CharField('留言标题', max_length=200, null=False)
    content = models.TextField('留言内容',)
    username = models.CharField('留言者姓名', max_length=200,)
    phone = models.CharField('留言者电话', max_length=200,)
    hittimes = models.IntegerField('阅读量', default=0)
    thumbup = models.IntegerField('点赞数', default=0)
    sort = models.PositiveIntegerField('排序', default=0)
    is_publish = models.BooleanField('是否发布', default=True)
    is_hide = models.BooleanField('是否隐藏', default=False)
    is_deleted = models.BooleanField('是否已删除', default=False)
    create_time = models.DateTimeField('添加时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)
    def __str__(self):
        return self.title
    class Meta:
        managed = True
        ordering = ['-sort']