from django import template
register = template.Library()


@register.filter
def inc(value: int, i=1) -> int:
    return value + i


@register.filter
def dec(value: int, i=1) -> int:
    return value - i