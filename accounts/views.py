from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView,DetailView,TemplateView,UpdateView,FormView,View,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate ,login
from . import forms
from .models import Profile
from django.contrib.auth.models import User
from django.views.generic.edit import FormMixin
from django.http import Http404
from job.models import Job


# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'


    def signup_user(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username,password=password)
                login = (request,user)
        else:
            form = self.form_class()

        return render(request, self.template_name, {'form': form})


class UserProfile(ListView):
    template_name = 'accounts/profile.html'
    model = Profile
    def your_view(self,request):
        profile = request.user.get_profile()
        return render(request,self.template_name,{'profile':profile})

    def get_queryset(self):
        try:
            self.job_user = User.objects.prefetch_related("job_owner").get(username__iexact=self.kwargs.get("username"))
            print(self.job_user)
        except User.DoesNotExist:
            raise Http404
        else:
            return self.job_user.job_owner.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["job_user"] = self.job_user
        print(context)
        return context


def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        userform = forms.UserForm(request.POST,instance=request.user)
        profileform = forms.ProfileForm(request.POST,request.FILES,instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))
    else:
        userform = forms.UserForm(instance=request.user)
        profileform = forms.ProfileForm(instance=profile)

    return render(request,'accounts/profile_edit.html',{'userform':userform,'profileform':profileform})
