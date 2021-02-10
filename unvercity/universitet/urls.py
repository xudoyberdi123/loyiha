from django.urls import path
from . import  views


urlpatterns = [
    path("", views.index, name ="index"),
    path("salom/" ,views.salom,name = "salom"),
    path("baza/",views.bazaa,name = "baza"),
    path("bazaa/", views.see, name="bazaa"),
]

