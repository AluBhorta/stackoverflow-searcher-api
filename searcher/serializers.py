
from rest_framework import serializers

from .models import QueryParam

# class QueryParamSerializer(serializers.ModelSerializer):
class QueryParamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QueryParam
        fields = "__all__"

