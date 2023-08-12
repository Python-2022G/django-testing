from django.http import HttpRequest, JsonResponse
from django.views import View
from django.forms.models import model_to_dict
from .models import Product
import json


class ProductListView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        products = Product.objects.all()

        data = [model_to_dict(product) for product in products]

        return JsonResponse(data, safe=False)


    def post(self, reqeust: HttpRequest) -> JsonResponse:
        data = json.loads(reqeust.body.decode('utf-8'))

        product = Product.objects.create(
            name=data['name'],  
            description=data['description'],
            price=data['price']
        )

        product.save()

        return JsonResponse(model_to_dict(product), status=201)

    