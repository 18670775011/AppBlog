from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View


class LoginView(View):
    """用户登录"""

    def get(self, request):
        return render(request, 'user/login.html')

    def post(self, request):
        """用户登录"""
        username = request.POST.get('username')
        password = request.POST.get('password')
        # fixme 开放其它用户登录注册
        # fixme 密码加密处理
        if username == 'admin' and password == 'admin123':
            return redirect(reverse('blog:index', args=[], current_app=self.request.resolver_match.namespace))
        else:
            # fixme 返回json数据，让前端提示
            return HttpResponse('用户名或密码错误')


class RegisterView(View):
    """用户注册"""
    # fixme 暂时不做用户注册功能，只通过管理员账户管理博客

    def get(self, request):
        pass

    def post(self, request):
        pass

