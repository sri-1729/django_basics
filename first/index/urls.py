from django.urls import path
from . import views

app_name = "ind"
urlpatterns = [
    path("", views.index, name="index"), #name is given for easy reference in our project
    path("addUsers", views.add, name="add"),
    path("deleteUsers", views.delete, name="del")
]
