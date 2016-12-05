from django import template
from blog.models import Post

register = template.Library()

@register.simple_tag()
def unpublished_posts():
    return Post.objects.filter(published_date__isnull=True).count()

@register.simple_tag()
def unapproved_comments(post):
    count = post.comments.count - post.approved_comments.count
    return count