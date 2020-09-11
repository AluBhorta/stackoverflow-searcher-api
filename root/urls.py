
from django.urls import include, path
from rest_framework import routers
from searcher.views import QueryParamViewSet

router = routers.DefaultRouter()
router.register(r'query-param', QueryParamViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
]
