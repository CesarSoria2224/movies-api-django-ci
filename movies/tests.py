from rest_framework.test import APITestCase
from rest_framework import status
from .models import Movie


class MovieAPITest(APITestCase):

    def test_create_movie(self):
        data = {
            "title": "Interstellar",
            "director": "Christopher Nolan",
            "release_year": 2014
        }

        response = self.client.post('/api/movies/', data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_movies(self):
        Movie.objects.create(
            title="Batman",
            director="Tim Burton",
            release_year=1989
        )

        response = self.client.get('/api/movies/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_movie(self):
        movie = Movie.objects.create(
            title="Old",
            director="Someone",
            release_year=2000
        )

        response = self.client.put(
            f'/api/movies/{movie.id}/',
            {
                "title": "New",
                "director": "Someone",
                "release_year": 2001
            }
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_movie(self):
        movie = Movie.objects.create(
            title="Delete Me",
            director="Director",
            release_year=2020
        )

        response = self.client.delete(f'/api/movies/{movie.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)