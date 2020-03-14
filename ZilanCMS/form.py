from django import forms
from ZilanCMS import models

class user_form(forms.ModelForm):
    class Meta:
        model = models.AllUser
        fields = ['username', 'phone', 'email', 'type', 'company','password']
        help_texts ={'username':''}
    def __init__(self, *args, **kwargs):
        super(user_form,self).__init__(*args, **kwargs)
        self.fields['username'].label = '姓名'
        self.fields['company'].required = False

class usertype_form(forms.ModelForm):
    class Meta:
        model = models.UserType
        fields = ['typename']
        # fields = []
    def __init__(self, *args, **kwargs):
        super(usertype_form,self).__init__(*args, **kwargs)

class uploadfile_form(forms.ModelForm):
    class Meta:
        model = models.UploadWork
        fields = ['filename', 'location', 'thumbnail', 'operate_illustrate', ]
    def __init__(self, *args, **kwargs):
        super(uploadfile_form,self).__init__(*args, **kwargs)




class article_form(forms.ModelForm):
    class Meta:
        model = models.BaseArticle
        fields = ['title', 'title2', 'note', 'content', 'type','sort','is_publish']

    def __init__(self, *args, **kwargs):
        super(article_form,self).__init__(*args, **kwargs)


class articletype_form(forms.ModelForm):
    class Meta:
        model = models.ArticleType
        fields = ['typename','tag','num']
        # fields = []
    def __init__(self, *args, **kwargs):
        super(articletype_form,self).__init__(*args, **kwargs)