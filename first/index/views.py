from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse

users = ["srijith"]

class userform(forms.Form):
    name = forms.CharField(label="New User")

# Create your views here.
def index(response):
    return render(response, "index/index.html",{
        "users" : users
    })

def add(response):
    if response.method == "POST":
        form = userform(response.POST)
        if form.is_valid():
            users.append(form.cleaned_data["name"])
            return HttpResponseRedirect(reverse("ind:index"))

    return render(response, "index/add.html",{
        "form": userform()

    })
