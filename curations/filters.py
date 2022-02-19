from dataclasses import field
import django_filters
from .models import Curation


class CurationFilter(django_filters.Filter):
    class Meta:
        model = Curation
        fields = "__all__"
