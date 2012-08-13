
from context_processor import site_pages
from django.shortcuts import render
from django.template import Context, loader
from django.http import HttpResponseServerError


def server_error(request, template_name='500.html'):
    t = loader.get_template(template_name)
    d = site_pages(request)
    return HttpResponseServerError(t.render(Context(d)))


def page_not_found_error(request, template_name='404.html'):
    t = loader.get_template(template_name)
    d = site_pages(request)
    return HttpResponseServerError(t.render(Context(d)))


def home(request):
    context = dict()
    if request.GET.get('o', None):
        context['open_integration'] = request.GET['o']
    return render(request, 'index.html', context)
