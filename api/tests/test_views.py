from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Book
from datetime import date

class BookViewTest(APITestCase):
    def test_response_is_correct(self):
        book = Book.objects.create(
            isbn = '12345',
	        title = "Demo",
	        description="Description",
            published_date = '2025-08-08',
	        author="Author"
	    )
        
        url = reverse('api:books')
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        body = response.json()
        returned_book = body[0]
        assert returned_book['isbn'] == book.isbn
        assert returned_book['title'] == book.title
        assert returned_book['description'] == book.description
        assert returned_book['published_date'] == book.published_date
        assert returned_book['author'] == book.author
		  
		
class HealthViewTest(APITestCase):
    def test_response_is_correct(self):
        url = reverse('api:health')
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        body = response.json()
        assert body['status'] == 'ok'
        
class BookDetailView(APITestCase):

    def setUp(self):
        self.book1 = Book.objects.create(
            isbn="12345AB",
            title="Test Book",
            description="Some description",
            author="Some Author",
            published_date=date (2025, 8, 8)
        )

    def test_get_book_by_isbn(self):
        response = self.client.get(f"/api/books/{self.book1.isbn}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)
        self.assertEqual(response.data["isbn"], self.book1.isbn)
        
    
    def test_delete_book (self):
        response = self.client.get(f"/api/books/{self.book1.isbn}/")
        response = self.client.delete(f"/api/books/{self.book1.isbn}/")
        assert response.status_code == 200   