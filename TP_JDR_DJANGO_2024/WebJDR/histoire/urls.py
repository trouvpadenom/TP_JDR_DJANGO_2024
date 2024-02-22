from django.urls import path
from .views import chap3, chap2, chap1, victoire, mort

urlpatterns = [
    path("mort/", mort, name="mort"),
    path("victoire/", victoire, name="victoire"),
    path("chap1/", chap1, name="chap1"),
    path('chap2/', chap2, name='chap2'),
    path('chap3/', chap3, name='chap3'),
]
