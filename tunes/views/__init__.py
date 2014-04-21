from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

class TunesIndexView(TemplateView):
    template_name = "tunes/index.html"
