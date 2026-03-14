from django.db import models
from django.utils.text import slugify
from common.models import BaseModel
from organizers.models import OrganizerProfile
from categories.models import Category
from venues.models import Venue


class Event(BaseModel):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
        ("cancelled", "Cancelled"),
        ("completed", "Completed"),
    ]

    organizer = models.ForeignKey(OrganizerProfile, on_delete=models.CASCADE, related_name="events")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="events")
    venue = models.ForeignKey(Venue, on_delete=models.SET_NULL, null=True, related_name="events")

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.CharField(max_length=300)
    full_description = models.TextField()

    cover_image = models.ImageField(upload_to="events/covers/", blank=True, null=True)

    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft")
    is_featured = models.BooleanField(default=False)
    published_at = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title