from django.shortcuts import render
from .models import BlogPost
# Create your views here.

def blog_post_detail_post(request):
    obj = BlogPost.objects.get(id=1)
    template_name = 'blog_post_detail'
    context = {'object': obj}
    return render( request, template_name, context)