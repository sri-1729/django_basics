from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse
from .models import users

class userform(forms.Form):
    name = forms.CharField(label="New User")
    motto = forms.CharField(label="Motto")

# Create your views here.
def index(response):
    x = users.objects.all()
    return render(response, "index/index.html",{
        "users" : x
    })

def add(response):
    if response.method == "POST":
        form = userform(response.POST)
        if form.is_valid():
            name=form.cleaned_data["name"]
            motto=form.cleaned_data["motto"]
            q = users(user_name = name, motto = motto)
            q.save()
            return HttpResponseRedirect(reverse("ind:index"))

    return render(response, "index/add.html",{
        "form": userform()

    })
