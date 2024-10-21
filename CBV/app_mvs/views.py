# from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from .serializer import CategorySerializer,SupplierSerializer,ProductSerializer
from .models import Category,Supplier,Products
from rest_framework.decorators import action
from rest_framework.response import Response

# create api view using modelViewSet 
class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
    # custom apis using action decorator 
    @action(detail=False,methods=['get'])
    def recent(self,request):
        category_model = self.queryset
        serializers = self.get_serializer(category_model,many=True)
        
        # serializer=serializers(category_model,many=True)
        return Response(serializers.data)
     
    #  if detail=true then it means it will act as working with single object 
    @action(detail=True,methods=['get'])
    def detail(self,request,pk=None):
        category = self.get_object()
        serializers = self.get_serializer(category)
        
        # serializer=serializers(category_model,many=True)
        return Response(serializers.data)
        


# using generic 
class SupplierGenericsListCreateApiView(ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierGenericsUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer



# model view set 

class ProductModelViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    
    # method override 
    # this fucntion will call to validate 
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    # it will run after validation 
    # def perform_create(self, serializer):
    #     category_id = serializer.validated_data.pop('category_id')
    #     supplier_id = serializer.validated_data.pop('supplier_id')
    #     # return super().perform_create(serializer)
        
    #     # category_obj = Category.objects.get(pk=category_id)
    #     # supplier_obj = Supplier.objects.get(pk=supplier_id)
        
    #     product = Products.objects.create(**serializer.validated_data,category = category_obj)
    #     product.supplier.set([supplier_obj])
    #     serializer = ProductSerializer(product)
    #     return Response(serializer.data)