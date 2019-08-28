from django.db import models


class BlogInfo(models.Model):
    """博客内容表"""
    title = models.CharField(max_length=50)
    content = models.TextField(null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    # Django会为每一个外键添加_id后缀
    user = models.ForeignKey('user.UserInfo', on_delete=models.DO_NOTHING)
    # fixme 对应分组被删后，移至默认分组
    type = models.ForeignKey('BlogGroup', on_delete=models.SET_DEFAULT, default=0)
    # 文章状态，0为草稿，1为发布
    status = models.IntegerField(max_length=1, default=0)

    class Meta:
        db_table = 'blog'


class BlogGroup(models.Model):
    """博客分组"""
    name = models.CharField(max_length=50)
    # fixme 后期允许在分组里面再建分组
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(null=True)

    class Meta:
        db_table = 'blog_group'

