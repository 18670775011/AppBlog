from django.db import transaction
from django.shortcuts import render
from django.views import View

from AppBlog.apps.blog.models import BlogInfo


class BlogView(View):
    """博客首页"""
    def get(self, request):
        return render(request, 'blog/index.html')


class BlogEditView(View):
    """博客编辑"""
    def get(self, request):
        return render(request, 'blog/editblog.html')

    @transaction.atomic
    def post(self, request):
        title = request.POST.get('title')
        content = request.POST.get('content')
        blog_type = request.POST.get('type')

        # 存入数据库
        blog = BlogInfo()
        blog.title = title
        blog.content = content
        blog.type = blog_type
        return render(request, 'blog/editblog.html', context={'title': title})
