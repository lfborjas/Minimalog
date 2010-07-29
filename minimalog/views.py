# Create your views here.
from django.shortcuts import render_to_response
from minimalog.forms import EntryForm
from minimalog.models import Entry
from django.http import HttpResponseRedirect
import functools
from django.conf import settings
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
PAGINATION = 3


@login_required
def new(request):
    """Create a new blog post"""
    if not request.user.is_staff:
        return HttpResponseRedirect('/blog/')
    
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            entry =  form.save()
            return HttpResponseRedirect(entry.get_absolute_url())
        else:
            return render_to_response('edit.html', {'form': form}, context_instance=RequestContext(request))
    else:
        return render_to_response('edit.html', {'form': EntryForm()}, context_instance=RequestContext(request))

def entry(request, slug):    
    entry = Entry.objects.filter(slug = slug)
          
    if not entry:
        return HttpResponseRedirect('/')    
    return render_to_response('list.html', {'entries': entry,
                                             'show_next': False,
                                             'comments': True,
                                             'debug': settings.DEBUG},
                                             context_instance=RequestContext(request))
    
def page(request, page_number=0):      
    ofs = int((PAGINATION*int(page_number))+PAGINATION)    
    show_next = bool(Entry.objects.all().order_by("-published")[ofs:(ofs+3)])
    page_ofs = int(PAGINATION*int(page_number))
    entries = Entry.objects.all().order_by("-published")[page_ofs:(page_ofs+3)]
        
    if page_number and not entries:
        return HttpResponseRedirect('/blog/')
    return render_to_response('list.html', {'entries': entries,
                                             'show_next': show_next,
                                             'comments': False,                                             
                                             'previous_page': int(page_number)+1},
                                             context_instance=RequestContext(request))
