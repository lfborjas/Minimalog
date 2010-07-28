from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to, direct_to_template
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^blog/', include('minimalog.urls')),
    (r'^contact/', direct_to_template, {'template': 'contact.html'}),
    (r'^$', redirect_to, {'url': '/blog/'}),
    # Example:
    # (r'^blog/', include('blog.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
