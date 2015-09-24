from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'reviewers.views.home', name='home'),
    url(r'^(?P<email>.*)$', 'reviewers.views.myPage', name='myPage'),
    url(r'^book/$', 'books.views.book', name='book'),
    # url(r'^blog/', include('blog.urls')),
)
