import json
import time
import logging

from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from AppBlog.apps.blog.form import GroupForm
from AppBlog.apps.blog.models import BlogInfo, BlogGroup

LOG = logging.getLogger('xxx.log')


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
        # TODO 存入数据库
        # blog.type = blog_type
        # blog.save()

        return render(request, 'blog/editblog.html', context={'title': title})


# 目前分组只支持一层分组，不支持分组内嵌套分组（后续可考虑，目前无太大意义）
class BlogGroup(View):
    """博客分组"""
    def get(self, request):
        res = {'success': 1}
        return HttpResponse(json.dumps(res), content_type="application/json")

    def post(self, request):
        if not GroupForm(request.POST).is_va0lid():
            LOG.error("Failed to check params!")

        g_name = request.POST.get('g_name')
        group = BlogGroup()
        group.name = g_name
        group.save()
        LOG.info("Success to save group! group name: %s" % g_name)
