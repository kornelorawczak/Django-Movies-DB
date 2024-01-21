import pytest
from core.data_operations import ApiOperations


@pytest.fixture
def database_operations():
    return ApiOperations()


@pytest.mark.django_db
class TestApiOperations:
    # This class tests (using pytest library) whether api operations work properly *(python manage.py runserver before launching the tests)
    def test_add_director(self, database_operations):
        # Tests whether adding a director through api works properly
        director_name = 'John Doe'
        director = database_operations.add_director(name=director_name)
        directors = database_operations.get_directors()
        assert director in directors
        database_operations.delete_director(director['id'])

    def test_delete_director(self, database_operations):
        # Tests whether deleting a director from database through api works properly
        director_name = 'John Doe'
        director = database_operations.add_director(name=director_name)
        database_operations.delete_director(director['id'])
        directors = database_operations.get_directors()
        assert director not in directors

    def test_getting_movies_for_director(self, database_operations):
        # Tests whether getting information about movies directed by the director from the database works properly through api
        director_name = 'John Doe'
        director = database_operations.add_director(name=director_name)
        movie_title = 'Test Movie'
        lead_actor_name = 'Test Actor'
        movie = database_operations.add_movie(
            title=movie_title, lead_actor_given=lead_actor_name, director_given=director_name
        )
        movies = database_operations.get_movies_for_director(director['id'])
        assert any(movie['title'] == movie_title for movie in movies)
        database_operations.delete_director(director['id'])
        database_operations.delete_movie(movie['id'])
