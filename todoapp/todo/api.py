from .models import Todo, Animal, AnimalClass, PlaceAnimal, Staff
from rest_framework import viewsets, permissions
from .serializers import TodoSerializer, AnimalSerializer, AnimalClassSerializer, PlaceAnimalSerializer, StaffSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TodoSerializer


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AnimalSerializer


class AnimalClassViewSet(viewsets.ModelViewSet):
    queryset = AnimalClass.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AnimalClassSerializer


class PlaceAnimalViewSet(viewsets.ModelViewSet):
    queryset = PlaceAnimal.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PlaceAnimalSerializer


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StaffSerializer
