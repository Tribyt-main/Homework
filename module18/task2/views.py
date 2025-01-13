from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def func_templates(request):
    return render(request, 'func_templates.html')
def main_page(request):
    return render(request, 'main_page.html')

class class_temp(TemplateView):
    template_name = 'class_templates.html'