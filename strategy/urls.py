from . import views
from django.urls import path


urlpatterns = [
    path('strategy/', views.strategybt, name='strategybt'),
]

