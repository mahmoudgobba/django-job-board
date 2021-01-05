from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView,ListView
from job.models import Categories,Job
from django.http import Http404


class CategoryList(ListView):
    template_name = "home/index.html"
    model = Categories

    def get_queryset(self):
        try:
            self.job_category = Job.objects.prefetch_related("category")
            # print(self.job_category)
        except Job.DoesNotExist:
            raise Http404
        else:
            return self.job_category.all()

    def get_context_data(self):
        object_list = Categories.objects.all()
        context = super().get_context_data()
        context["job_category"] = self.job_category
        # print(context)
        # return context
        return ({'context':context,'object_list':object_list})
