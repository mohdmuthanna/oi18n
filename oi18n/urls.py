from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'oi18n.views.home', name='home'),
    url(r'^', 'blog.views.home'),

    url(r'^admin/', include(admin.site.urls)),
]
