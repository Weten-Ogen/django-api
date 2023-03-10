# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.models import Product
from product.serializers import ProductSerializer


# Create your views here.
@api_view(["POST"])
def api_home(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        print(serializer.data)
        data= serializer.data 

    # instance = Product.objects.all().order_by('?').first()
    # data = {}
    # if instance:
    #     data = ProductSerializer(instance).data
        return Response(data)
