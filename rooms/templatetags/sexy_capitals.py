from django import template

register = template.Library()


@register.filter
def sexy_capitals(value):
    print(value)
    return "lalalala"
