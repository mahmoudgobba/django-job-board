from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import View,ListView,DetailView,CreateView,DeleteView
from . import models
from .forms import ApplyForm,CreateForm
from django.views.generic.edit import FormMixin
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .filters import JobFilter
from django.http import Http404,HttpResponseRedirect



# Create your views here.
def JobsListView(request):
    job_list2 = models.Job.objects.all().order_by("-id")
    job_list = models.Job.objects.all().order_by("-id")
    job_filter = JobFilter(request.GET, queryset=job_list)
    job_list = job_filter.qs
    # sorted_results = sorted(job_list, key= lambda t: date.published_at())
    paginator = Paginator(job_list,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'jobs':page_obj,'job_filter':job_filter,'job_list2':job_list2}
    return render(request, 'job/job_list.html',context)






class JobsDetailView(DetailView,FormMixin):
    model = models.Job
    form_class = ApplyForm
    template_name = 'job/job_detail.html'

        # Handle POST GTTP requests
    def post(self, request, *args, **kwargs):
        job_apply = get_object_or_404(models.Job,kwargs={'slug':self.kwargs.get('slug')})
        if request.method == 'POST':
            form = self.form_class(request.POST,request.FILES)
            if form.is_valid():
                myform = form.save(commit=False)
                myform.job = job_apply
                myform.save()
                myform.clean_fields()
            return HttpResponseRedirect(reverse('jobs:job_detail',kwargs={'slug':self.kwargs.get('slug')}))

        else:
            form = self.form_class()

        return render(request, self.template_name, {'form': form},)


@method_decorator(login_required, name='dispatch')
class CreateJob(CreateView,LoginRequiredMixin):
    model = models.Job
    form_class = CreateForm
    template_name = 'job/job_add.html'
    success_url = reverse_lazy("jobs:all")

    def job_ad(self, request, *args, **kwargs):
        user = User.objects.get(username=request.user.username)
        if request.method == 'POST':
            form = self.form_class(request.POST)
            if form.is_valid():
                myform = form.save(commit=False)
                myform.owner = request.user
                print(request.user)
                myform.save()
                myform.clean_fields()
        else:
            form = self.form_class()

        return render(request, self.template_name, {'form': form})


class UserJobs(ListView):
    model = models.Job
    template_name = "job/user_jobs_list.html"

    def get_queryset(self):
        try:
            self.job_user = User.objects.prefetch_related("job_owner").get(username__iexact=self.kwargs.get("username"))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.job_user.job_owner.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["job_user"] = self.job_user
        return context

class DeleteJob(DeleteView):
    success_url = reverse_lazy("jobs:all")
    model = models.Job
