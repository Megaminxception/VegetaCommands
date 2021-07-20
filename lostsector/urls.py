from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("lostsector", views.lost_sector_vegeta, name="lost sector vegeta"),
    path("lostsectordiscord", views.today_lost_sector, name="lost sector defaul"),
]

