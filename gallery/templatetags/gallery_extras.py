from django.template import Library

register = Library()


@register.filter
def get_range(value):
    return range(value)


@register.filter
def is_mod_3(value):
    return value % 3 == 0