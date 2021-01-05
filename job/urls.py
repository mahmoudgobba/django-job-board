from django.urls import path,include
from . import views
from django_filters.views import FilterView
from .filters import JobFilter
from.models import Job

app_name = 'job'


urlpatterns = [
    path('',views.JobsListView,name='all'),
    path('add/',views.CreateJob.as_view(),name='add_job'),
    path('<slug:pk>/',views.JobsDetailView.as_view(),name='job_detail'),
    path('delete/<slug:pk>/',views.DeleteJob.as_view(),name='delete'),
    path('by/<str:username>/',views.UserJobs.as_view(),name='for_user'),
]
