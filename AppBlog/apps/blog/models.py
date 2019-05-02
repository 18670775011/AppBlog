from django.db import models


class BlogContent(models.Model):
    """博客内容表"""
    title = models.CharField(max_length=50)
    content = models.TextField(null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    # Django会为每一个外键添加_id后缀
    auth = models.ForeignKey('BlogAuth', on_delete=models.DO_NOTHING)
    # fixme 对应分组被删后，移至默认分组
    type = models.ForeignKey('BlogGroup', on_delete=models.SET_DEFAULT, default='default_group')


class BlogGroup(models.Model):
    """博客分组"""
    name = models.CharField(max_length=50)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)


class BlogAuth(models.Model):
    """博客作者"""
    name = models.CharField(max_length=50)
    age = models.IntegerField(max_length=3, null=True)
    email = models.EmailField(null=True)
    # fixme 允许用户上传头像，未上传就使用默认头像
    user_pic = models.ImageField(upload_to='icons', height_field='url_height',
                                 width_field='url_width', default='icons/default.jpg')
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
