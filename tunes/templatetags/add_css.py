from django import template

register = template.Library()

def add_class(field, css):
    return field.as_widget(attrs={"class":css})

register.filter('add_class', add_class)
