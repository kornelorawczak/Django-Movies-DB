from datetime import datetime

from core.data_operations import ApiOperations, DatabaseOperations
from core.models import Actors, Directors, Movies
from django.core.management.base import BaseCommand, CommandParser
from django.db.utils import IntegrityError


class Command(BaseCommand):
    # This class is responsible for implementing a text client for the directors model (python manage.py directors ...)
    help = 'Add a new Director figure to the DataBase. In order to do that you shall pass --add flag followed by --name, --date_of_birth, --latest_movie'

    def add_arguments(self, parser):
        parser.add_argument(
            '--mode', choices=['database', 'api'], default='database', help='Choose data access mode')
        parser.add_argument('--write', action='store_true',
                            help='Flag --write is necessary to write out the contents of database')
        parser.add_argument('--add', action='store_true',
                            help='Flag --add is necessary to add a director to the DB')
        parser.add_argument(
            '--delete', type=int, help='Use this flag to delete a record from selected table, follow it with number >0 that indicates which record you want to get rid of')
        parser.add_argument(
            '--movies', type=int, help=f'This flag will query through DB and write out info about movies directed by selected director. To select a director write a positive number after the flag ')
        parser.add_argument(
            '--name', type=str, help='Full name of a director, prefferably using Capital letters and good name format')
        parser.add_argument('--date_of_birth', type=str,
                            help='date of birth of a director in format YYYY/MM/DD')
        parser.add_argument('--latest_movie', type=str,
                            help='Title of a latest movie directed by the given director')

    def handle(self, *args, **kwargs):
        mode = kwargs['mode']
        # depending on the 'mode' flag actions will be performed locally or through the api (defaultly its set for the local handling)
        if mode == 'database':
            database_operations = DatabaseOperations()
        elif mode == 'api':
            database_operations = ApiOperations()

        if kwargs['add']:
            # Adding 'add' flag means user is trying to create a director record, in order to do that its necessary to pass at least directors' name
            name = kwargs['name']
            date_of_birth = kwargs['date_of_birth']
            latest_movie = kwargs['latest_movie']
            database_operations.add_director(name, date_of_birth, latest_movie)

        elif kwargs['write']:
            # 'write' flag is reponsible for writing out data about all the directors in the database
            directors = database_operations.get_directors()
            for i, director in enumerate(directors):
                self.stdout.write(f"{director['id']}. {director['name']} born on {
                                  director['date_of_birth']}. The latest movie he/she directed is called {director['latest_movie']}")

        elif kwargs['delete']:
            # 'delete' flag is responsible for deleting a director from the database, you shall pass his/her index
            record_number = kwargs['delete']
            database_operations.delete_director(record_number)

        elif kwargs['movies']:
            # 'movies' flag will show data about all the movies directed by selected - by index - director
            director_id = kwargs['movies']
            movies = database_operations.get_movies_for_director(director_id)
            if movies:
                for i, movie in enumerate(movies):
                    self.stdout.write(f'{i+1}. "{movie["title"]}" released on {movie["premiere_date"]} starring {
                                      movie['lead_actor']} has won {movie['academy_awards']} Academy Awards.')
        else:
            self.stdout.write(self.style.ERROR(
                'You need to present at least one valid main flag! Type --help to get more info'))
