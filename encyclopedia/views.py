import markdown2


from django import forms
from django.shortcuts import render

from . import util
from markdown2 import Markdown

markdowner = Markdown()


class Search(forms.Form):
    item = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Search'}))


class Edit(forms.Form):
    textarea = forms.CharField(widget=forms.Textarea(), label='')


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, entry):
    entryPage = util.get_entry(entry)
    if entryPage is None:
        return render(request, "encyclopedia/nonExistingEntry.html", {
            "entryTitle": entry
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "entry": markdowner.convert(entryPage),
            "entryTitle": entry
        })


def create(request):
    return render(request, "encyclopedia/create.html", {

    })


def edit(request, title):
    return render(request, "encyclopedia/edit.html", {

    })
