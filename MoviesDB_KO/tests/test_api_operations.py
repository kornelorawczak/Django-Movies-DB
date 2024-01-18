import pytest
from core.data_operations import ApiOperations


@pytest.fixture
def database_operations():
    return ApiOperations()


@pytest.mark.django_db
class TestApiOperations:
    def test_add_director(self, database_operations):
        director_name = 'John Doe'
        director = database_operations.add_director(name=director_name)
        directors = database_operations.get_directors()
        assert director in directors
        database_operations.delete_director(director['id'])

    def test_delete_director(self, database_operations):
        director_name = 'John Doe'
        director = database_operations.add_director(name=director_name)
        database_operations.delete_director(director['id'])
        directors = database_operations.get_directors()
        assert director not in directors

    def test_getting_movies_for_director(self, database_operations):
        director_name = 'John Doe'

        # Dodaj reżysera
        director = database_operations.add_director(name=director_name)

        # Dodaj film
        movie_title = 'Test Movie'
        lead_actor_name = 'Test Actor'
        movie = database_operations.add_movie(
            title=movie_title, lead_actor_given=lead_actor_name, director_given=director_name
        )

        # Sprawdź, czy film jest zwracany poprawnie dla danego reżysera
        movies = database_operations.get_movies_for_director(director['id'])
        assert any(movie['title'] == movie_title for movie in movies)

        # Usuń reżysera i film
        database_operations.delete_director(director['id'])
        database_operations.delete_movie(movie['id'])
