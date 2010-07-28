'''
Created on 27/07/2010

@author: lfborjas
'''
from django import forms
from minimalog.models import Entry
from google.appengine.ext import db

class EntryForm(forms.Form):
    title = forms.CharField(widget=forms.widgets.TextInput(attrs={'class': 'edit'}))
    slug = forms.CharField(widget=forms.widgets.TextInput(attrs={'class': 'edit'}))
    body = forms.CharField(widget=forms.widgets.Textarea(attrs={'class': 'body-edit edit'}))
    
    def clean_slug(self):
        slug = self.cleaned_data['slug']
        if db.Query(Entry).filter("slug =", slug).count():
            raise forms.ValidationError("Duplicated url... Please choose another one")
        else:
            return slug