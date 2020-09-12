
from django.urls import include, path
from rest_framework import routers
from searcher.views import QueryParamViewSet, QuestionViewSet, ShallowUserViewSet

router = routers.DefaultRouter()
router.register(r'query-params', QueryParamViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'users', ShallowUserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
