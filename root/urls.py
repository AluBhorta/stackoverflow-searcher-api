
from django.urls import path
from searcher import views


urlpatterns = [
    path('api/search/', views.search_view, name='search'),
]
