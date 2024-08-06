from django.utils.http import urlencode
from django import template

from goods.models import Categories


register = template.Library()

@register.simple_tag()
def tag_categories():
    return Categories.objects.all()

@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    que = context['request'].GET.dict()
    que.update(kwargs)
    return urlencode(que)