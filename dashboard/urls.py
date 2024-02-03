from django.urls import path, include
from .dash_apps import scatter, histogram
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('django_plotly_dash', include('django_plotly_dash.urls')),
    path('index.html', views.dashboard_view, name='dashboard'),
    # Other URL patterns...
]