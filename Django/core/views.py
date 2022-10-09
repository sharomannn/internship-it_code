from django.shortcuts import render
from django.utils import timezone
from core import models

def index(request):
    now = timezone.now()
    person = models.Person.objects.first
    return render(request, 'core/index.html', context={'dt':now, 'person':person})