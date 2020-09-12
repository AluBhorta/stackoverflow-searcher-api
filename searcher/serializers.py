
from rest_framework import serializers

from .models import QueryParam, Question, ShallowUser


class QueryParamSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueryParam
        fields = "__all__"


class ShallowUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShallowUser
        fields = "__all__"


class QuestionParamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"
