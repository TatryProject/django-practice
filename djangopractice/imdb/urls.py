from django.urls import path
from . import views

urlpatterns = [
  path("list", views.get_titles, name="list"),
  path("<str:tconst>", views.detail, name="detail"),
]