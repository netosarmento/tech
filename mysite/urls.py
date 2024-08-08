from . import views
from .views import home_page, servicos, contatos, sobre, ceo
from django.urls import path, include

urlpatterns = [
    path('', home_page, name="home_page"),
    path('servicos/', servicos, name="servicos"),
    path('contatos/', contatos, name="contatos"),
    path('sobre/', sobre, name="sobre"),
    path('ceo/', ceo, name="ceo"),
]
