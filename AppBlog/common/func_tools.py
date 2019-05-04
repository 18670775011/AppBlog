import hashlib
import uuid

from AppBlog.settings import MDEIA_ROOT
import os

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin123'


def default_user_pic_path():
    r"""
    兼容windows和linux的用户默认头像路径
    :return: static/user/icons/default.jpg 或 static\user\icons\default.jpg
    """
    _path = os.path.join(os.path.join(os.path.join(MDEIA_ROOT, 'user'), 'icons'), 'default.jpg')
    return _path


def encrypt_pw(password):
    """
    密码加密处理
    :param password:需要加密的密码
    :return:SHA512加密的密码
    """
    sha = hashlib.sha512()
    sha.update(password.encode('utf-8'))
    return sha.hexdigest()


def uuid_str(name):
    """
    基于名字的 SHA-1 散列值
    :param name:基于的名字
    :return:SHA-1 散列值
    """
    return str(uuid.uuid5(uuid.uuid4(), name))
