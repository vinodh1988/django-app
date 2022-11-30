from rest_framework.decorators import APIView
from firstapi.models import Product
from firstapi.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status

class ProductAPI(APIView):
    def get(self,request,pk=None):
        products=Product.objects.all()
        result=ProductSerializer(products,many=True)
        return Response(result.data)

    def post(self,request):
        record=ProductSerializer(data=request.data)
        try:
            if(record.is_valid()):
                record.save()
                return Response(record.data)
            else:
                return Response({'error':'not valid record'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({'error':'server error'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
       

                   