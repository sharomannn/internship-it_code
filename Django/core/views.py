import json

from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from core import models
from core import filters
from core import serializers
from django.views.generic import TemplateView, ListView
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework import status

class TagViewSet(ReadOnlyModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.Tag
    filterset_class = filters.Tag


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
    serializer = serializers.TagSearch(data=request.GET)
    if not serializer.is_valid():
        return JsonResponse(serializer.errors, status=400)

    f = filters.Tag(request.GET, queryset=models.Tag.objects.all())
    serializer = serializers.Tag(instance=f.qs, many=True)
    return JsonResponse({'result':serializer.data})