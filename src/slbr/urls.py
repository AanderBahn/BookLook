from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^newBook/$', 'reviewers.views.newBook', name='newBook'),
    url(r'^newReview/$', 'reviewers.views.newReview', name='newReview'),
    url(r'^$', 'reviewers.views.home', name='home'),
    url(r'^testHome$', 'slbr.views.testHome', name='testHome'),
    url(r'^(?P<name>.*)/$', 'reviewers.views.myPage', name='myPage'),
    # url(r'^blog/', include('blog.urls')),
)
