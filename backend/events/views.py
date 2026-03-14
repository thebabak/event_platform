from rest_framework import generics
from .models import Event
from .serializers import EventListSerializer, EventDetailSerializer


class EventListAPIView(generics.ListAPIView):
    queryset = Event.objects.filter(status="published").order_by("start_datetime")
    serializer_class = EventListSerializer


class EventDetailAPIView(generics.RetrieveAPIView):
    queryset = Event.objects.filter(status="published")
    serializer_class = EventDetailSerializer
    lookup_field = "slug"