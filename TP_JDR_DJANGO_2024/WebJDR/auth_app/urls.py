from django.urls import path
from .views import redirect_to_last_visited

urlpatterns = [
    path('redirect-to-last-visited/', redirect_to_last_visited, name='redirect_to_last_visited'),
]
