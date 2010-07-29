from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import redirect_to, direct_to_template
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib.auth.views import login, logout
admin.autodiscover()

urlpatterns = patterns('',
    (r'^blog/', include('minimalog.urls')),
    (r'^contact/', direct_to_template, {'template': 'contact.html'}),
    #(r'^projects/', direct_to_template, {'template': 'projects.html'}),
    (r'^$', redirect_to, {'url': '/blog/'}),
    # Example:
    # (r'^blog/', include('blog.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    #These are already provided by django!
    (r'login/', login, {'template_name': 'login.html'}),
    (r'logout/', logout, {'next_page': '/blog/'}),
)

if settings.DEBUG:
    urlpatterns += patterns('',       
        (r'^images/(?P<path>.*)$', redirect_to, {'url': '/static/images/%(path)s'}),
        (r'^css/(?P<path>.*)$', redirect_to, {'url': '/static/css/%(path)s'}),
        (r'^js/(?P<path>.*)$', redirect_to, {'url': '/static/js/%(path)s'}),
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),
    )
