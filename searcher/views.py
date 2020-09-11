
# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions

from .models import QueryParam
from .serializers import QueryParamSerializer


class QueryParamViewSet(viewsets.ModelViewSet):
    queryset = QueryParam.objects.all().order_by('sort')
    serializer_class = QueryParamSerializer
    permission_classes = [permissions.AllowAny]
