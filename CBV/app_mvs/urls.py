from django.urls import path
from .views import CategoryModelViewSet,SupplierGenericsListCreateApiView,SupplierGenericsUpdateDestroyApiView,ProductModelViewSet
from rest_framework.routers import DefaultRouter

# for modelviewset
router = DefaultRouter()
router.register('category',CategoryModelViewSet)
router.register('products',ProductModelViewSet)
# urlpatterns = 

# for generic view set 
urlpatterns = [
    path('suppliers/',SupplierGenericsListCreateApiView.as_view()),
    path('suppliers/<pk>',SupplierGenericsUpdateDestroyApiView.as_view()),
] +router.urls
