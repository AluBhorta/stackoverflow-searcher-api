from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import viewsets, permissions, status
import requests

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

    # db_query_param = QueryHandler(
    #     search_query_params
    # ).get_query_param_from_db()

    # if db_query_param == None:
    #     # make api call to SO.
    #     # save (QueryParam, Question[], SearchResult) to DB
    #     # update quota
    #     # return out
    #     pass

    # else send result matching pk of db_query_param

    # mvp
    so_api_url = "https://api.stackexchange.com/2.2/search/advanced"
    params = {
        "q": search_query_params.get("q"),
        "body": search_query_params.get("body"),
        "title": search_query_params.get("title"),
        "url": search_query_params.get("url"),
        "tagged": search_query_params.get("tagged"),
        "nottagged": search_query_params.get("nottagged"),
        "answers": search_query_params.get("answers"),
        "views": search_query_params.get("views"),
        "user": search_query_params.get("user"),
        "page": search_query_params.get("page"),
        "pagesize": search_query_params.get("pagesize"),
        "accepted": search_query_params.get("accepted"),
        "closed": search_query_params.get("closed"),
        "migrated": search_query_params.get("migrated"),
        "wiki": search_query_params.get("wiki"),
        "notice": search_query_params.get("notice"),
        "order": search_query_params.get("order"),
        "sort": search_query_params.get("sort"),
        "min": search_query_params.get("min"),
        "max": search_query_params.get("max"),
        "fromdate": search_query_params.get("fromdate"),
        "todate": search_query_params.get("todate"),
        "site": "stackoverflow",
    }

    so_response = requests.get(so_api_url, params=params)
    results = so_response.json().get('items')

    out = {
        "quota_daily_limit": 100,
        "quota_minute_limit": 5,
        "quota_daily_remain": 100,
        "quota_minute_remain": 5,

        "query_params": params,
        "results": results,
        "count": len(results),

        "links": {
            "previous": "",
            "next": "",
        }
    }
    return Response(out)
