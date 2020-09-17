
from rest_framework import serializers

from .models import Question, ShallowUser, QueryHash


class QueryHashSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueryHash
        fields = "__all__"

class ShallowUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShallowUser
        fields = "__all__"


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"
