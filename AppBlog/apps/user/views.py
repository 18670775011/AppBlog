from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from AppBlog.apps.user.models import UserInfo
from AppBlog.common.func_tools import encrypt_pw, uuid_str

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin123'


class LoginView(View):
    """用户登录"""

    def get(self, request):
        return render(request, 'user/login.html')

    def post(self, request):
        """用户登录"""
        username = request.POST.get('username')
        password = encrypt_pw(request.POST.get('password'))
        user_infos = UserInfo.objects.filter(user_name=username, password=password)

        # 登录成功，更新token
        if user_infos.exists():
            user_info = user_infos.first()
            token = uuid_str(username)
            request.session['token'] = token
            user_info.token = token
            return redirect(reverse('blog:index', args=[], current_app=self.request.resolver_match.namespace))
        else:
            # fixme 返回json数据，让前端提示
            return HttpResponse('用户名或密码错误')


class RegisterView(View):
    """用户注册"""

    def get(self, request):
        return render(request, 'user/register.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        # fixme 前端js对密码进行加密处理
        # fixme 前后端都增加数据格式效验以及用户是否存在效验
        # 存入数据库,目前不对用户名邮箱格式进行效验
        self._create_user(request, username, password, email)
        # 返回session
        return redirect(reverse('blog:index', args=[], current_app=self.request.resolver_match.namespace))

    def _create_user(self, request, username, password, email):
        user_info = UserInfo()
        user_info.user_name = username
        user_info.password = encrypt_pw(password)
        user_info.email = email
        token = uuid_str(username)
        user_info.token = token
        request.session['token'] = token
        try:
            user_info.save()
        except Exception as ex:
            # fixme 日志记录报错信息
            return HttpResponse('创建用户失败，请重试或联系管理员！')