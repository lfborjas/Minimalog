# Create your views here.
from django.shortcuts import render_to_response
from minimalog.forms import EntryForm
from minimalog.models import Entry
from google.appengine.api import users
from django.http import HttpResponseRedirect
from google.appengine.ext import db
PAGINATION = 3
import functools
from django.conf import settings
from django.template import RequestContext

def administrator(method):
    @functools.wraps(method)
    def wrapper(request, *args, **kwargs):
        user = users.get_current_user()
        if not user:
            #if request.method == "GET":
            return HttpResponseRedirect(users.create_login_url(request.path))               
            
        elif not users.is_current_user_admin():
            return HttpResponseRedirect('/')
        else:
            return method(request, *args, **kwargs)
    return wrapper

@administrator
def new(request):
    """Create a new blog post"""
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            user = users.get_current_user()
            title = form.cleaned_data['title']
            slug = form.cleaned_data['slug']
            body = form.cleaned_data['body']
            entry = Entry(title= title,
                          slug= slug,
                          body = body,
                          author= user)
            entry.put()
            return HttpResponseRedirect(entry.get_absolute_url())
        else:
            return render_to_response('edit.html', {'form': form}, context_instance=RequestContext(request))
    else:
        return render_to_response('edit.html', {'form': EntryForm()}, context_instance=RequestContext(request))

def entry(request, slug):
    entry = db.Query(Entry).filter("slug =", slug).fetch(limit=1)
    if not entry:
        return HttpResponseRedirect('/')
    
    return render_to_response('list.html', {'entries': entry,
                                             'show_next': False,
                                             'comments': True,
                                             'debug': settings.DEBUG},
                                             context_instance=RequestContext(request))
    
def page(request, page_number=0):      
    ofs = int((PAGINATION*int(page_number))+PAGINATION)    
    show_next = bool(db.Query(Entry).order("-published").fetch(limit=3, offset=(ofs)))
    entries = db.Query(Entry).order("-published").fetch(limit=3, offset=int(PAGINATION*int(page_number)))
    if page_number and not entries:
        return HttpResponseRedirect('/blog/')
    return render_to_response('list.html', {'entries': entries,
                                             'show_next': show_next,
                                             'comments': False,
                                             'debug': settings.DEBUG,
                                             'previous_page': int(page_number)+1},
                                             context_instance=RequestContext(request))
