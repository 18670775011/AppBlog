from django.conf.urls import url
from AppBlog.apps.blog.views import BlogView, BlogEditView

urlpatterns = [
    url(r'^$', BlogView.as_view(), name='index'),
    url(r'^edit$', BlogEditView.as_view(), name='editblog'),
]
