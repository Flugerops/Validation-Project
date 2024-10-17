import unittest
from fastapi.testclient import TestClient
from app import app


class TestApi(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_create_book_valid_data(self):
        response = self.client.post(
            "/create_book",
            json={
                "title": "Sample Book",
                "author": "John Doe",
                "year": 2023,
                "genre": "Fiction",
                "isbn": "978-3-16-148410-0",
            },
        )
        self.assertEqual(response.status_code, 201)

    def test_create_book_invalid_isbn(self):
        response = self.client.post(
            "/create_book",
            json={
                "title": "Sample Book",
                "author": "John Doe",
                "year": 2023,
                "genre": "Fiction",
                "isbn": "978-3-16-148410",
            },
        )
        self.assertEqual(response.status_code, 422)

    def test_create_book_invalid_year(self):
        response = self.client.post(
            "/create_book",
            json={
                "title": "Future Book",
                "author": "Jane Doe",
                "year": 2025,
                "genre": "Fiction",
                "isbn": "978-3-16-148410-0",
            },
        )
        self.assertEqual(response.status_code, 422)


if __name__ == "__main__":
    unittest.main()
