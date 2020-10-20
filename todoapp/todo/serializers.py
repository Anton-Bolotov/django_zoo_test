from rest_framework import serializers
from .models import Todo, Animal, AnimalClass, PlaceAnimal, Staff


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'


class AnimalClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalClass
        fields = '__all__'


class PlaceAnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceAnimal
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'
