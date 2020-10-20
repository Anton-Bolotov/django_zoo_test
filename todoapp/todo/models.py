from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=150, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Animal(models.Model):
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    created_at = models.DateTimeField()
    name_animal = models.CharField(max_length=30)
    number_of_limbs = models.IntegerField()
    area = models.CharField(max_length=30)
    life_style = models.CharField(max_length=30)
    animal_class = models.CharField(max_length=30)

    def __str__(self):
        return self.name_animal


class AnimalClass(models.Model):
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    created_at = models.DateTimeField()

    animal_group = models.CharField(max_length=30)
    animal_family = models.CharField(max_length=30)
    animal_kind = models.ForeignKey(Animal, on_delete=models.CASCADE)
    animal_type = models.CharField(max_length=30)
    red_book = models.CharField(max_length=30)

    def __str__(self):
        return self.animal_family


class PlaceAnimal(models.Model):
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    created_at = models.DateTimeField()
    date_cleaning = models.DateTimeField()
    type = models.ForeignKey(Animal, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    area_placements = models.CharField(max_length=255)
    biom = models.CharField(max_length=255)

    def __str__(self):
        return self.address


class Staff(models.Model):
    updated_at = models.DateTimeField(auto_now_add=True, blank=True)
    created_at = models.DateTimeField()
    staff_name = models.CharField(max_length=30)
    position = models.CharField(max_length=30)
    area_of_responsibility = models.ForeignKey(PlaceAnimal, on_delete=models.CASCADE)
    pinned_animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    pay = models.IntegerField()
    work_time_animal = models.IntegerField()

    def __str__(self):
        return self.staff_name





