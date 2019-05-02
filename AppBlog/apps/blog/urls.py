from django.conf.urls import url
from AppBlog.apps.blog import views
from AppBlog.apps.blog.views import BlogView


urlpatterns = [
    url(r'^$', BlogView.as_view(), name='index'),
]
