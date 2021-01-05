import django_filters
from .models import Job
from django import forms


class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    # location = django_filters.CharFilter(label = "PI Name")
    class Meta:
        model = Job
        fields = ('title','job_type','description','category','location','salary','experience')
