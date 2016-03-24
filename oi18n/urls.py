from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'blog.views.home'),
    url(r'^walli$', 'blog.views.walli'),

    url(r'^admin/', include(admin.site.urls)),
]
