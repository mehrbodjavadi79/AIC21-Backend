from django.db import models
from model_utils.models import TimeStampedModel, UUIDModel
from django.conf import settings


class Map(TimeStampedModel, UUIDModel):
    name = models.CharField(max_length=256, unique=True)
    file = models.FileField(upload_to=settings.UPLOAD_PATHS["MAP"])
