from django.urls import path
import core.views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', core.views.Index.as_view()),

    path('tags/', core.views.tags),
    path('persons/', core.views.Person.as_view()),
]

router = DefaultRouter()
router.register('tags', core.views.TagViewSet, basename="tag")
urlpatterns += router.urls

