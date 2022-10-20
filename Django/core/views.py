import json

from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from core import models
from core import filters
from django.views.generic import TemplateView, ListView

class Index(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        c = super().get_context_data(**kwargs)
        c['person_name'] = 'Roma'
        return c

class Person(ListView):
    model = models.Person

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        return response


def index(request):
    now = timezone.now()
    person = models.Person.objects.first()
    return render(request, 'core/index.html',
                  context={'dt': now, 'person': person})


# def person(request):
#     object_list = []
#     for p in models.Person.objects.all():
#         object_list.append({
#             'id': p.id,
#             'name': p.name,
#             'number' : p.phone,
#         })
#     # content = json.dumps(object_list)
#     return JsonResponse({'objects' : object_list}, status=400)


def tags(request):
    f = filters.Tag(request.GET, queryset=models.Tag.objects.all())

    return JsonResponse({'result':list(f.qs.values())})