from django.shortcuts import render
from rest_framework.views import  APIView
from rest_framework.response import Response

# Create your views here.

#Book Resource
#/api/books

class HealthView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(
            {
                "status":"ok"
            }
            
        )
        
 #instantiate the object in Django
health_view = HealthView.as_view()





class BookView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(
            {
                "hello":"django"
            }
            
        )
        
 #instantiate the object in Django
book_view = BookView.as_view()