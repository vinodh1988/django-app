from rest_framework.decorators import APIView
from firstapi.models import Product
from firstapi.serializers import ProductSerializer
from rest_framework.response import Response

class ProductAPI(APIView):
    def get(self,request,pk=None):
        products=Product.objects.all()
        result=ProductSerializer(products,many=True)
        return Response(result.data)