from django.urls import path
from . import views

urlpatterns = [
    path("shoez/<int:pk_shoe>/", views.shoez, name="shoez"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("create_run/", views.create_run, name="create_run")
    ]