from django import template

register = template.Library()

@register.filter
def key_to_value(d, key_name):
    value = 0
    try:
        value = eval("d."+key_name)

    except KeyError:
        value = 0
    return value