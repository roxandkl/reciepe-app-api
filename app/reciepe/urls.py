from django.urls import path, include
from rest_framework.routers import DefaultRouter

from reciepe import views

router = DefaultRouter()
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)
router.register('reciepes', views.ReciepeViewSet)

app_name = 'reciepe'

urlpatterns = [
    path('', include(router.urls))
]