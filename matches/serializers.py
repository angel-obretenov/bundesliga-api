from rest_framework import serializers


class MatchesSerializer(serializers.Serializer):
    groupName = serializers.CharField()
    groupOrderID = serializers.IntegerField()
    groupID = serializers.IntegerField()
