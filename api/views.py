from django.shortcuts import render
from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer
from .models import Book


#Book Resource
#/api/books

class HealthView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(
            {
                "status":"200"
            } )
        
 #instantiate the object in Django
health_view = HealthView.as_view()


class BookView(APIView):
    
    ####List all books or create a new book    
    def get(self, request, *args, **kwargs):
        all_books = Book.objects.all()
        serializer = BookSerializer(all_books, many=True)
        return Response(serializer.data)
        
        ####Create a new book
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = BookSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (serializer.data)
    
    #def delete(self, request, isbn)
    
class BookDetailView(APIView):
     
    def get(self, request, isbn):
        book = Book.objects.get(isbn=isbn)
        serialiser = BookSerializer(book)
        return Response(serialiser.data)
    
    def put(self, request, isbn):
        book = Book.objects.get(isbn=isbn)
        serialiser = BookSerializer(instance=book, data=request.data)
        serialiser.is_valid(raise_exception=True)
        serialiser.save()
        return Response(serialiser.data)
    
    def delete(self, request, isbn):
        book = Book.objects.get(isbn=isbn)
        book.delete()
        return Response({"Book has been delete"})
     
    
     #instantiate the object in Django
book_view = BookView.as_view()
book_detail_view = BookDetailView.as_view()