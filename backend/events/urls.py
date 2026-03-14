from django.urls import path
from .views import EventListAPIView, EventDetailAPIView

urlpatterns = [
    path("", EventListAPIView.as_view(), name="event-list"),
    path("<slug:slug>/", EventDetailAPIView.as_view(), name="event-detail"),
]