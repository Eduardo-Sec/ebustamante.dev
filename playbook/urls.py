from django.urls import path

from . import views

app_name = "playbook"

urlpatterns = [
    path("", views.index, name="index"),
    path("offense/", views.offense, name="offense"),
    path("defense/", views.defense, name="defense"),
    path("special-teams/", views.special, name="special"),
    path("card/", views.card, name="card"),
]
