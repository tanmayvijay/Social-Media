from django import template
from ..models import Post
from django.utils.safestring import mark_safe
import markdown


register = template.Library()


@register.simple_tag
def total_posts():
	return Post.published.count()



@register.filter(name='markdown')
def markdown_format(text):
	return mark_safe(markdown.markdown(text))