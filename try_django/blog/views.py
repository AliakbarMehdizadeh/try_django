from django.shortcuts import render
from .models import BlogPost
from django.http import Http404
# Create your views here.

def blog_post_detail(request, slug):
    try:
        obj = BlogPost.objects.get(slug=slug)
    except:
        raise Http404
    template_name = 'blog_post_detail.html'
    context = {'object': obj}
    return render( request, template_name, context)