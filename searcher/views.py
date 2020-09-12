from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import viewsets, permissions, status

from .models import QueryParam, Question, ShallowUser
from .serializers import QueryParamSerializer, QuestionParamSerializer, ShallowUserSerializer
from .quota import QuotaValidator
from .query import QueryHandler


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
    if not QuotaValidator().has_quota():
        return Response({
            "message": "No quota remaining"
        }, status=status.HTTP_400_BAD_REQUEST)

    search_query_params = request.query_params.dict()

    db_query_param = QueryHandler(
        search_query_params
    ).get_query_param_from_db()

    if db_query_param == None:
        # make api call to SO.
        # save (QueryParam, Question[], SearchResult) to DB
        # update quota
        pass

    
    # else send result matching pk of db_query_param

    out = {
        "message": "Great success!",
        "quota_daily_limit": 100,
        "quota_minute_limit": 5,
        "quota_daily_remain": 100,
        "quota_minute_remain": 5,
        "search_query_params": search_query_params,
        "questions": []

    }
    return Response(out)
