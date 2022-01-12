from django.contrib.auth.models import Permission
from django.db.models.query import QuerySet
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Reciepe, Tag, Ingredient
from reciepe import serializers

class BaseReciepeAttrViewSet(viewsets.GenericViewSet, 
                             mixins.ListModelMixin,
                             mixins.CreateModelMixin):
    """Base Viewset for user owned reciepe attribute"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Return object for current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        """Create a new tag"""
        serializer.save(user=self.request.user)


class TagViewSet(BaseReciepeAttrViewSet):
    """Manage Tags in database"""
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer


class IngredientViewSet(BaseReciepeAttrViewSet):
    """Manage Ingredients in the database"""
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer


class ReciepeViewSet(viewsets.Modelviewset):
    """Manage Recipe in database"""
    serializer_class = serializers.ReciepeSerializer
    queryset = Reciepe.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Retrive reciepe for authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-name')
