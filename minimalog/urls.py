from django.conf.urls.defaults import *

urlpatterns = patterns('minimalog.views',
    (r'^$', 'page'),                   
    (r'^page/(?P<page_number>\d+)/$', 'page'),
    (r'^entry/new/$', 'new'),
    (r'^entry/(?P<slug>[-\w\d]+)/$', 'entry'),        
    #(r'^edit/(?P<entry_id>\d+)/$', 'edit'),
    #It should be trivial to add archival mapping: (like entry/year/month/slug), but it's not *necessary* now         
 )