from django import template
from django.db.models.aggregates import Count

from ..models import Post,Category

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def archives():
    return Post.objects.dates('created_time','month',order='DESC')

@register.simple_tag
def get_categories():
    return Category.objects.annotate(
        num_post=Count('post')
    ).filter(num_post__gt=0)