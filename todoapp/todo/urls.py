from rest_framework import routers
from .api import TodoViewSet, AnimalViewSet, AnimalClassViewSet, StaffViewSet, PlaceAnimalViewSet


router = routers.DefaultRouter()
router.register('api/todo', TodoViewSet, 'todo')
router.register('api/animal', AnimalViewSet, 'animal')
router.register('api/animalclass', AnimalClassViewSet, 'animalclass')
router.register('api/staff', StaffViewSet, 'staff')
router.register('api/place', PlaceAnimalViewSet, 'place')


urlpatterns = router.urls
