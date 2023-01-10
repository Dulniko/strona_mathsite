from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ranking/", views.ranking, name="ranking"),
    path("mnozenie/", views.mnozenie, name="mnozenie"),
    path("mnozenie10/", views.mnozenie10, name="mnozenie10"),
]
