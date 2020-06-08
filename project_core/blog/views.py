from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from .models import Blog


def all_blogs(request):
    blogs = Blog.objects.order_by('-date')

    paginator = Paginator(blogs, 10)
    page = request.GET.get('page')
    paged_blogs = paginator.get_page(page)

    context = {
        'blogs': paged_blogs
    }

    return render(request, 'blog/all_blogs.html', context)

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':blog})