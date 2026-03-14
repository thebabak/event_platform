from django.db import models
from common.models import BaseModel
from accounts.models import User


class OrganizerProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="organizer_profile")
    brand_name = models.CharField(max_length=255)
    legal_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.brand_name