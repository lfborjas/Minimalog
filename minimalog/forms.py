'''
Created on 27/07/2010

@author: lfborjas
'''
from django import forms
from minimalog.models import Entry


class EntryForm(forms.ModelForm):
    title = forms.CharField(widget=forms.widgets.TextInput(attrs={'class': 'edit'}))
    slug = forms.CharField(widget=forms.widgets.TextInput(attrs={'class': 'edit'}))
    body = forms.CharField(widget=forms.widgets.Textarea(attrs={'class': 'body-edit edit'}))
    
    class Meta:
        model = Entry
        exclude = ('author',)
    