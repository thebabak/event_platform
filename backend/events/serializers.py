from rest_framework import serializers
from .models import Event


class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "slug",
            "short_description",
            "start_datetime",
            "end_datetime",
            "status",
            "is_featured",
        ]


class EventDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"