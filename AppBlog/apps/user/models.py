from django.db import models
from AppBlog.common.func_tools import default_user_pic_path

DEFAULT_USER_PIC_PATH = default_user_pic_path()


class UserInfo(models.Model):
    """用户信息表"""
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=250)
    email = models.EmailField(max_length=50, null=True)
    # fixme 允许用户上传头像，未上传就使用默认头像
    user_pic = models.ImageField(upload_to='icons', default=DEFAULT_USER_PIC_PATH)
    # 账户状态（注销后变成False）
    status = models.BooleanField(default=True)
    # 用户等级(999: 超级用户， 1：普通用户)
    level = models.IntegerField(default=1)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'user'
