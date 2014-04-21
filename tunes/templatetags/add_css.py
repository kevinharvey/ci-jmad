from django import template

register = template.Library()

def add_class_to_field(field, css):
    return field.as_widget(attrs={"class":css})

register.filter('add_class_to_field', add_class_to_field)
