from django.conf.urls import url
from rest_framework import routers
from api.views import MathOperationsView

router = routers.DefaultRouter()

urlpatterns = router.urls

urlpatterns += {
    url(r'^math', MathOperationsView.as_view(), name='math_operation')
}