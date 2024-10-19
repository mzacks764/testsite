from django.urls import path
from . import views   # . means from the current directory


# URL patters are the allowable URL

urlpatterns = [
    path("", views.index, name="index"),                #when user visit the empty path display view.index
    path("michael", views.michael, name = "michael"),
    path("<str:name>", views.greet,name = "greet")             # greet takes a parameter name so any name after hello/name is used to diplay greet ULL
]