from django import template
register=template.Library()
import re

@register.filter
def hide_email(val):
    s=re.sub('^.....','*****',val)
    return s

    
    