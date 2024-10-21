from rest_framework import serializers
from .models import Category,Supplier,Products

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"
        


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    supplier = SupplierSerializer(read_only=True,many=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(),write_only=True)
    supplier_id = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all(),write_only=True,many=True)

    class Meta:
        model = Products
        fields = ['name','id','category','supplier','category_id','supplier_id']
        
        # this function will run at last
    def create(self, validated_data):
        category_id = validated_data.pop('category_id')
        supplier_id = validated_data.pop('supplier_id')
        
        product = Products.objects.create(**validated_data,category = category_id)
        product.supplier.set(supplier_id)
        serializer = ProductSerializer(product)
        return serializer.data 
        
                