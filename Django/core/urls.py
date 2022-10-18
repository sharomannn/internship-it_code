from django.urls import path
import core.views

urlpatterns = [
    path('', core.views.Index.as_view()),
    path('person/', core.views.Person.as_view()),
]
