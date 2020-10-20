from django.contrib import admin
from .models import Todo, Animal, AnimalClass, PlaceAnimal, Staff


class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'date', 'done')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'description')
    list_editable = ('done',)
    list_filter = ('done',)


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('id', 'updated_at', 'created_at', 'name_animal', 'number_of_limbs', 'area', 'life_style',
                    'animal_class')
    list_display_links = ('id', 'name_animal')
    search_fields = ('id', 'name_animal', 'life_style')
    list_filter = ('name_animal',)


class PlaceAnimalAdmin(admin.ModelAdmin):
    list_display = ('id', 'updated_at', 'created_at', 'date_cleaning', 'type', 'address', 'area_placements', 'biom')
    list_display_links = ('id', 'area_placements')
    search_fields = ('id', 'area_placements', 'biom')
    list_filter = ('area_placements', )


class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'updated_at', 'staff_name', 'position', 'area_of_responsibility', 'pinned_animal', 'pay',
                    'work_time_animal')
    list_display_links = ('id', 'staff_name')
    search_fields = ('id', 'staff_name', 'pinned_animal')
    list_filter = ('work_time_animal', 'pinned_animal')


class AnimalClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'updated_at', 'animal_group', 'animal_family', 'animal_kind', 'animal_type', 'red_book')
    list_display_links = ('id', 'animal_group')
    search_fields = ('id', 'animal_group', 'animal_type')
    list_filter = ('animal_group',)


admin.site.register(Todo, TodoAdmin)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(PlaceAnimal, PlaceAnimalAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(AnimalClass, AnimalClassAdmin)
