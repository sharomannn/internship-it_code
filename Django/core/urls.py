from django.urls import path
import core.views
from rest_framework.routers import DefaultRouter

app_name = 'core'

urlpatterns = [
    path('user/register/', core.views.RegisterUser.as_view(), name='user_register'),
    path('user/login/', core.views.LoginUser.as_view()),
]

router = DefaultRouter()
router.register('tags', core.views.TagViewSet, basename='tag')
router.register('items', core.views.ItemViewSet, basename='item')

urlpatterns += router.urls

