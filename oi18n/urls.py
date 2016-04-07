from django.conf.urls import include, url
from django.contrib import admin
from solid_i18n.urls import solid_i18n_patterns


urlpatterns = solid_i18n_patterns('',
    # Examples:
    url(r'^$', 'blog.views.home'),
    url(r'^walli$', 'blog.views.walli'),

    url(r'^admin/', include(admin.site.urls)),
)
