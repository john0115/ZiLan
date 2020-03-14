# rest_framework 序列化文件
from ZilanCMS.models import AllUser,UploadWork,FileType
from rest_framework import serializers,viewsets,permissions,decorators,renderers,authentication
from django.http import HttpResponse
from ZilanCMS.permissiions import IsOwnerOrReadOnly,IsManagerOrReadModifyOnly,NoDelate,NoDelateManager

# -----------------------Initialize  Serializer -------------------------#
class AllUserSerializer(serializers.HyperlinkedModelSerializer):
    # 显示外键为本User的列表id
    # uploadwork = serializers.PrimaryKeyRelatedField(many=True, queryset=UploadWork.objects.all())
    class Meta:
        model = AllUser
        fields = ['id', 'username','password',  'nickname', 'phone', 'shot', ]
    ## 重写User 写入函数
    def create(self, validated_data):
        return AllUser.objects.create_user(**validated_data)


class UploadWorkSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = UploadWork
        fields = ['filename', 'file_illustrate' ,'location', 'thumbnail', 'user']
class FileTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FileType
        fields = ['typename']

# -----------------------Initialize  ViewSet -------------------------#
class AllUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows AllUser to be viewed or edited.
    """
    permission_classes = [permissions.IsAuthenticated,
                          IsManagerOrReadModifyOnly,NoDelateManager]

    queryset = AllUser.objects.all().order_by('-date_joined')
    serializer_class = AllUserSerializer
class UploadWorkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows AllUser to be viewed or edited.
    """
    queryset = UploadWork.objects.all().order_by('-update_time')
    serializer_class = UploadWorkSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    #增加detail下面具体值的获取
    @decorators.action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def filename(self, request, *args, **kwargs):
        file = self.get_object()
        return HttpResponse(file.filename)
    #操作时将request.user自动添加为user的instance
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FileTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows AllUser to be viewed or edited.
    """
    # authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = FileType.objects.all().order_by('-typename')
    serializer_class = FileTypeSerializer

