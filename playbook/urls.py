from django.urls import path

from . import views

app_name = "playbook"

urlpatterns = [
    path("", views.index, name="index"),
    path("rules/", views.rules, name="rules"),
    path("offense/", views.offense, name="offense"),
    path("defense/", views.defense, name="defense"),
    path("special-teams/", views.special, name="special"),
    path("glossary/", views.glossary, name="glossary"),
    path("card/", views.card, name="card"),
]
