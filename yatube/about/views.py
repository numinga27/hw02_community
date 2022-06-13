from django.shortcuts import render
from django.views.generic.base import TemplateView



class AboutAuthorView(TemplateView):
    template_name = 'app_name/about/author.html'


class AboutTechView(TemplateView):
    template_name = 'app_name/about/tech.html'

