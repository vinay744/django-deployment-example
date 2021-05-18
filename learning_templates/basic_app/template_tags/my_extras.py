from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):

    # THIS CUTS OUT ALL THE VALUES OF "ARG" FROM THE STRING!

    return value.replace(arg,'')

# register.filter('cut',cut)