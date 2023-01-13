from django.urls import path
from . import views

urlpatterns = [
    path("", views.mainpage, name="mainpage"),
    path("rankingi/", views.rankingi, name="rankingi"),
    path("ranking10/", views.ranking10, name="ranking10"),
    path("ranking50/", views.ranking50, name="ranking50"),
    path("mnozenie/", views.mnozenie, name="mnozenie"),
    path("mnozenie10/", views.mnozenie10, name="mnozenie10"),
    path("mnozenie50/", views.mnozenie50, name="mnozenie50"),
    path('profile/', views.profile.as_view(), name='profile'),
]
