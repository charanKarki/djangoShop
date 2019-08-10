from django.shortcuts import render
from django.views import View
from .serializers import productSerializer
from rest_framework import serializers
from django.http import JsonResponse,HttpResponse
from .models import products
# Create your views here.

class shopAppView(View):
    def get(self,request):
        
        return render(request,'index.html',{'title':'shop Website'})


def productsView(request):
    items= productSerializer(products.objects.all(),many=True)
    return JsonResponse(items.data,safe=False)

def itemDetail(request):
    return render(request,'itemDetail.html',{'title':'Item Details'})