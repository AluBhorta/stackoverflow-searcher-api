from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
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


@api_view()
def search_view(request: Request):
    """ 
    # pseudocode

    quota not left for quota_minute or quota_daily?
        return error
    does request.query_params exists in QueryParam table?
    yes:
        find the corresponding SearchResult
        return SearchResult
    no:
        fetch SearchResult from stackoverflow
        save (QueryParam, Question[], SearchResult) to DB
        return SearchResult

    """

    out = {
        "quota_daily": 100,
        "quota_minute": 5,
        "query_params": request.query_params,
        "users": [user.display_name for user in ShallowUser.objects.all()],
        "questions": [question.title for question in Question.objects.all()],
    }
    return Response(out)
