from django.http import HttpResponse

from django.views.generic import TemplateView # Import TemplateView


class Index(TemplateView):
    template_name = "index.html"
