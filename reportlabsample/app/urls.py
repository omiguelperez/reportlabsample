from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .reports import customer_report
from .views import CustomerViewSet

router = DefaultRouter()
router.register(r'customers', CustomerViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]

reporturls = [
    url(r'^customer-report/', customer_report),
]

urlpatterns += reporturls
