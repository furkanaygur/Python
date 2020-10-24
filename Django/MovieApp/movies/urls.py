from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='movies'),
    path('<int:movies_id>', views.details, name='detail'),
    path('search', views.search, name='search'),
]