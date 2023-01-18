from django.urls import path
from . import views

urlpatterns = [
    path("", views.mainpage, name="mainpage"),
    path("rankingi/", views.rankingi, name="rankingi"),
    path("ranking/<int:nr_of_questions>/", views.ranking, name="ranking"),
    path("mnozenie/", views.SelOfMult, name="SelOfMult"),
    path("mnozenie/<int:nr_of_questions>/", views.Multiplication, name="Multiplication"),
    path('profile/', views.profile.as_view(), name='profile'),
    path("profile/delete/<slug:username>", views.deleteAccount.as_view(), name="deleteAcc"),
]
