from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import viewsets, permissions, status
import requests

from .models import QueryHash, Question, ShallowUser
from .serializers import QueryHashSerializer, QuestionSerializer, ShallowUserSerializer
from .quota import QuotaValidator
from .util import get_dict_hash


@api_view()
def search_view(request: Request):
    quota_validator = QuotaValidator()
    if not quota_validator.has_quota():
        return Response({
            "message": "Error! No quota remaining!"
        }, status=status.HTTP_400_BAD_REQUEST)

    search_query_params = request.query_params.dict()
    query_param = {
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

    qp_hash = get_dict_hash(query_param)

    try:
        qh = QueryHash.objects.get(pk=qp_hash)
        qh_data = QueryHashSerializer(qh).data

        has_more = qh_data.get("has_more")

        try:
            question_id_strings = qh_data.get("question_ids").split(",")
            question_ids = [int(qid) for qid in question_id_strings]
        except:
            question_ids = []

        questions = [Question.objects.get(question_id=qid)
                     for qid in question_ids]

        questions = [QuestionSerializer(question).data
                     for question in questions]

        for question in questions:
            try:
                user = ShallowUser.objects.get(
                    user_id=(question.get("owner"))
                )
                user_data = ShallowUserSerializer(user).data
                question["owner"] = user_data
            except ShallowUser.DoesNotExist:
                question["owner"] = None

            question["tags"] = question.get("tags", "").split(",")

        is_new = False
    except QueryHash.DoesNotExist:
        so_api_url = "https://api.stackexchange.com/2.2/search/advanced"

        so_response = requests.get(so_api_url, params=query_param)
        if so_response.status_code != 200:
            return Response({
                "message": "Error! Bad request!"
            }, status=status.HTTP_400_BAD_REQUEST)

        so_response = so_response.json()
        has_more = so_response.get('has_more')
        questions = so_response.get('items', [])

        for question in questions:
            try:
                user = ShallowUser.objects.get(
                    user_id=question.get("owner").get("user_id")
                )
            except ShallowUser.DoesNotExist:
                user = ShallowUser(
                    user_id=question.get("owner").get("user_id"),
                    reputation=question.get("owner").get("reputation"),
                    display_name=question.get("owner").get("display_name"),
                    profile_image=question.get(
                        "owner").get("profile_image", ""),
                    link=question.get("owner").get("link", ""),
                    user_type=question.get("owner").get("user_type")
                )
                user.save()

            tags = ",".join([t for t in question.get("tags", [])])

            try:
                ques = Question.objects.get(
                    question_id=question.get("question_id")
                )
            except Question.DoesNotExist:
                ques = Question(
                    question_id=question.get("question_id"),
                    is_answered=question.get("is_answered"),
                    view_count=question.get("view_count"),
                    answer_count=question.get("answer_count"),
                    score=question.get("score"),
                    last_activity_date=question.get("last_activity_date"),
                    creation_date=question.get("creation_date"),
                    content_license=question.get("content_license", ""),
                    title=question.get("title", ""),
                    link=question.get("link", ""),
                    tags=tags or "",
                    owner=user,
                )
                ques.save()

        question_id_list = [str(question.get("question_id"))
                            for question in questions]
        question_ids = ','.join(question_id_list)

        qh = QueryHash.objects.create(
            query_param_hash=qp_hash,
            question_ids=question_ids,
            has_more=has_more
        )

        is_new = True

    remaining_quota = quota_validator.get_remaining_quota()

    out = {
        "quota_daily_remain": remaining_quota.get("daily_quota", 0),
        "quota_minute_remain": remaining_quota.get("minute_quota", 0),
        "is_new": is_new,
        "count": len(questions),
        "has_more": has_more,
        "message": "Great Success!",
        "questions": questions,
    }
    return Response(out)
