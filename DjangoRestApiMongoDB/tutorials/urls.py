from django.urls import include, path
from rest_framework import routers
from django.conf.urls import url
from . import views

router = routers.DefaultRouter()
router.register(r'api_tutorial', views.TutorialViewSet)
router.register(r'api_movie', views.MovieViewSet)
router.register(r'api_test1', views.Test1ViewSet)
router.register(r'api_test2', views.Test2ViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),


]
