from django.urls import path
from . import views

urlpatterns = [
    path('guitars/', views.GuitarsPage.as_view(), name='guitars'),
]