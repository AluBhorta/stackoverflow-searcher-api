
from django.urls import include, path
from rest_framework import routers
from searcher import views

router = routers.DefaultRouter()

router.register(r'query-params', views.QueryParamViewSet)
router.register(r'questions', views.QuestionViewSet)
router.register(r'users', views.ShallowUserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('search/', views.search_view, name='search'),
]
