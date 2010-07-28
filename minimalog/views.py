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

def administrator(method):
    @functools.wraps(method)
    def wrapper(request, *args, **kwargs):
        user = users.get_current_user()
        if not user:
            if request.method == "GET":
                return HttpResponseRedirect(users.create_login_url(request.path))               
            
        elif not users.is_current_user_admin():
            return HttpResponseRedirect('/')
        else:
            return method(request, *args, **kwargs)
    return wrapper

#@administrator
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
            return render_to_response('edit.html', {'form': form})
    else:
        return render_to_response('edit.html', {'form': EntryForm()})

def entry(request, slug):
    entry = db.Query(Entry).filter("slug =", slug).fetch(limit=1)
    if not entry:
        return HttpResponseRedirect('/')
    
    return render_to_response('list.html', {'entries': entry,
                                             'show_more': False,
                                             'comments': True,
                                             'debug': settings.DEBUG})
    
def page(request, page_number):
    return render_to_response('list.html', {'entries': db.Query(Entry).fetch(limit=3, offset=PAGINATION*page),
                                             'show_more': False,
                                             'comments': True,
                                             'debug': settings.DEBUG})
