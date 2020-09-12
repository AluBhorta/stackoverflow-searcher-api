
# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions

from .models import QueryParam, Question, ShallowUser
from .serializers import QueryParamSerializer, QuestionParamSerializer, ShallowUserSerializer


class QueryParamViewSet(viewsets.ModelViewSet):
    queryset = QueryParam.objects.all().order_by('sort')
    serializer_class = QueryParamSerializer
    permission_classes = [permissions.AllowAny]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('last_activity_date')
    serializer_class = QuestionParamSerializer
    permission_classes = [permissions.AllowAny]


class ShallowUserViewSet(viewsets.ModelViewSet):
    queryset = ShallowUser.objects.all().order_by('user_id')
    serializer_class = ShallowUserSerializer
    permission_classes = [permissions.AllowAny]
