from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include(('health.urls', 'health'), namespace='health')),
    url(r'^', include(('api.urls', 'api'), namespace='api'))
]
