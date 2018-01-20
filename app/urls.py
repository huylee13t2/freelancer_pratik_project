
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from app import views
from rest_framework.schemas import get_schema_view

router = DefaultRouter()
router.register(r'city', views.CityViewSet)
router.register(r'locality', views.LocalityViewSet)
router.register(r'property-type', views.PropertyTypeViewSet)
router.register(r'society', views.SocietyViewSet)
schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^', include(router.urls)),
]