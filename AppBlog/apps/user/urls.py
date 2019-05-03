from django.conf.urls import url
from AppBlog.apps.user.views import LoginView


urlpatterns = [
    url(r'^login$', LoginView.as_view(), name='login'),
]
