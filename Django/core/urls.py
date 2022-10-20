from django.urls import path
import core.views

urlpatterns = [
    path('', core.views.Index.as_view()),
    path('tags', core.views.tags),
    path('person/', core.views.Person.as_view()),
]
