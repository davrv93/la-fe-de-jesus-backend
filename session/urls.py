from rest_framework import routers
from django.conf.urls import url, include
from session.views.session import SessionViewSet
from session.views.content import ContentViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'sessions', SessionViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'contents', ContentViewSet.as_view(), name='contents' )
]
