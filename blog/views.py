from django.shortcuts import render
from blog.models import Post,Comment
from django.views.generic import ListView
from django.core.paginator import Paginator

# Create your views here.

def postsListView(request):
    post_list2 = Post.objects.all().order_by("-id")
    post_list = Post.objects.all().order_by("-id")
    # post_filter = JobFilter(request.GET, queryset=job_list)
    # post_list = job_filter.qs
    paginator = Paginator(post_list,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'posts':page_obj,'job_list2':post_list2}
    return render(request, 'blog/blog.html',context)

class CommentList(ListView):
    model = Comment
    template_name = "blog/blog.html"
