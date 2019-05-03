from AppBlog.settings import MDEIA_ROOT
import os


def default_user_pic_path():
    r"""
    兼容windows和linux的用户默认头像路径
    :return: static/user/icons/default.jpg 或 static\user\icons\default.jpg
    """
    _path = os.path.join(os.path.join(os.path.join(MDEIA_ROOT, 'user'), 'icons'), 'default.jpg')
    return _path
