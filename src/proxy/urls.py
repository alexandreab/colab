
from django.conf.urls import patterns, include, url

from .views import TracProxyView, JenkinsProxyView, GitlabProxyView, RedmineProxyView , SvnProxyView


urlpatterns = patterns('',
    # Trac URLs
    url(r'^(?P<path>(?:admin|wiki|changeset|newticket|ticket|chrome|timeline|roadmap|browser|report|tags|query|about|prefs|log|attachment|raw-attachment|diff|milestone).*)$',
        TracProxyView.as_view()),

    # Trac URLs
    url(r'^trac/(?P<path>.*)$', TracProxyView.as_view()),


    # Gitlab URLs
    url(r'^gitlab/(?P<path>.*)$', GitlabProxyView.as_view()),

    # Gitlab
    url(r'^users/(?P<path>.*)$', GitlabProxyView.as_view()),

    # Jenkins URLs
    url(r'^ci/(?P<path>.*)$', JenkinsProxyView.as_view()),

    # SVN
    url(r'^svn/(?P<path>.*)$', SvnProxyView.as_view()),

    #url(r'^projects/(?P<path>.*)$', RedmineProxyView.as_view()),
    url(r'^redmine/(?P<path>.*)$', RedmineProxyView.as_view()),

)






