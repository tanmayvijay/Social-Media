# imports
from django import template
from django.utils.safestring import mark_safe
import markdown
from ..models import Post



register = template.Library()

# # to find the no of published posts
# @register.simple_tag
# def total_posts():
# 	return Post.published.count()



# to apply markdown to posts
@register.filter(name='markdown')
def markdown_format(text):
	return mark_safe(markdown.markdown(text))