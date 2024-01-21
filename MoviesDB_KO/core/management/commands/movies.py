from datetime import datetime

from core.data_operations import ApiOperations, DatabaseOperations
from core.models import Actors, Directors, Movies
from django.core.management.base import BaseCommand, CommandParser
from django.db.utils import IntegrityError


class Command(BaseCommand):
    # This class is responsible for implementing a text client for the movies model (python manage.py movies ...)
    help = 'Use --add followed by --title, --premiere_date, --director, --category, --lead_actor, --academy_awards to add a new Movie to the database. \n Use --write to write out all the \
        movies that currently are in database'

    def add_arguments(self, parser):
        parser.add_argument(
            '--mode', choices=['database', 'api'], default='database', help='Choose data access mode')
        parser.add_argument('--write', action='store_true',
                            help="Flag --write is necessary to write the contents of database")
        parser.add_argument('--add', action='store_true',
                            help='Flag --add is necessary to add a movie to the DB')
        parser.add_argument(
            '--delete', type=int, help='Use this flag to delete a record from selected table, follow it with number >0 that indicates which record you want to get rid of')
        parser.add_argument('--title', type=str, help='Title of a movie')
        parser.add_argument('--premiere_date', type=str,
                            help='Premiere_date of a movie in format YYYY/MM/DD')
        parser.add_argument('--director', type=str, help=f'Full name of a director: {
                            [dir.name for dir in Directors.objects.all()]}')
        parser.add_argument('--category', type=str, help='Category of a movie')
        parser.add_argument('--lead_actor', type=str, help=f'Full name of lead actor: {
                            [actor.name for actor in Actors.objects.all()]}')
        parser.add_argument('--academy_awards', type=int,
                            help='Number of oscars won by the movie. Pass the number 0-11')

    def handle(self, *args, **kwargs):
        mode = kwargs['mode']
        # depending on the 'mode' flag actions will be performed locally or through the api (defaultly its set for the local handling)
        if mode == 'database':
            database_operations = DatabaseOperations()
        elif mode == 'api':
            database_operations = ApiOperations()

        if kwargs['add']:
            # 'add' flag is reponsible for adding a movie record to the database.
            # You need to pass at least a title, director and actor (both of them shall be passed as a name)
            # If there won't be an actor/director with given name in the database, they will be created
            title = kwargs['title']
            premiere_date = kwargs.get('premiere_date', None)
            if premiere_date != None:
                premiere_date = datetime.strptime(
                    premiere_date, '%Y-%m-%d').date()
            director_given = kwargs['director']
            category = kwargs.get('category', None)
            lead_actor_given = kwargs['lead_actor']
            academy_awards = kwargs.get('academy_awards', None)
            database_operations.add_movie(
                title, lead_actor_given, director_given, premiere_date, category, academy_awards)

        elif kwargs['write']:
            # 'write' flag is reponsible for outputting data about all the movies in the database
            movies = database_operations.get_movies()
            for i, movie in enumerate(movies):
                self.stdout.write(f'{movie['id']}. "{movie['title']}" ({movie['category']}) premiered {movie['premiere_date']}. It was directed by {
                                  movie['director']} and starred {movie['lead_actor']}. It won {movie['academy_awards']} academy awards.')
        elif kwargs['delete']:
            # 'delete' flag will delete a movie of index matching passed one
            record_number = kwargs['delete']
            database_operations.delete_movie(record_number)
        else:
            self.stdout.write(self.style.ERROR(
                "You need to present at least one valid main flag! Type --help to get more info"))
