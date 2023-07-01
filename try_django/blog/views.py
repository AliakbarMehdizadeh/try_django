from django.shortcuts import render
from .models import BlogPost
from django.http import Http404
# Create your views here.

def blog_post_list_view(request):
    qs = BlogPost.objects.all()
    template_name = 'blog_post_list.html'
    context = { 'object_list': qs }
    return render(request, template_name, context)

def blog_post_create_view(request):
    template_name = 'blog_post_create.html'
    context = { 'form': None}
    return render(request, template_name, context)

def blog_post_detail_view(request,slug):
    obj = BlogPost.objects.get(slug=slug)
    template_name = 'blog_post_detail.html'
    context = {'object': obj}
    return render( request, template_name, context)

def blog_post_update_view(request, slug):
    obj = BlogPost.objects.get(slug=slug)
    template_name = 'blog_post_update_view.html'
    context = {'object': obj}
    return render( request, template_name, context)

def blog_post_delete_view(request,slug):
    obj = BlogPost.objects.get(slug=slug)
    template_name = 'blog_post_delete_view.html'
    context = {'object': obj}
    return render( request, template_name, context)