import pytest
from core.data_operations import DatabaseOperations
from core.models import Actors, Movies


@pytest.fixture
def database_operations():
    return DatabaseOperations()


@pytest.mark.django_db
class TestDatabaseOperations:
    # Class that tests whether certain operations on local database works correctly
    def test_add_actor(self, database_operations):
        # Adding actor to the database locally test
        actor_name = "John Doe"
        database_operations.add_actor(name=actor_name)
        assert Actors.objects.filter(name=actor_name).exists()

    def test_add_delete_actor(self, database_operations):
        # deleting actor from the database locally test
        actor_name = "John Doe"
        database_operations.add_actor(name=actor_name)
        actor = Actors.objects.get(name=actor_name)
        database_operations.delete_actor(actor.id)
        assert not Actors.objects.filter(name=actor_name).exists()

    def test_movie_from_actor(self, database_operations):
        # Tests whether getting data from the database locally about movie starring certain actor works properly 
        database_operations.add_movie(title="Test Movie", lead_actor_given="Test Actor", director_given="Test Director")
        assert Movies.objects.filter(title="Test Movie").exists()
        actor = Actors.objects.get(name="Test Actor")
        movies = database_operations.get_movies_for_actor(actor.id)
        assert "Test Movie" == movies[0]["title"]
