from datetime import datetime

from core.models import Directors
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Add a new Director figure to the DataBase. In order to do that you shall pass --add flag followed by --name, --date_of_birth, --latest_movie'

    def add_arguments(self, parser):
        parser.add_argument(
            '--write', action='store_true', help='Flag --write is necessary to write out the contents of database'
        )
        parser.add_argument('--add', action='store_true', help='Flag --add is necessary to add a director to the DB')
        parser.add_argument(
            '--delete',
            type=int,
            help='Use this flag to delete a record from selected table, follow it with number >0 that indicates which record you want to get rid of',
        )
        parser.add_argument(
            '--movies',
            type=int,
            help=f'This flag will query through DB and write out info about movies directed by selected director. To select a director write a positive number after the flag ',
        )
        parser.add_argument(
            '--name', type=str, help='Full name of a director, prefferably using Capital letters and good name format'
        )
        parser.add_argument('--date_of_birth', type=str, help='date of birth of a director in format YYYY/MM/DD')
        parser.add_argument('--latest_movie', type=str, help='Title of a latest movie directed by the given director')

    def handle(self, *args, **kwargs):
        if kwargs['add']:
            name = kwargs['name']
            date_of_birth = (
                datetime.strptime(kwargs['date_of_birth'], '%Y-%m-%d').date() if kwargs['date_of_birth'] else None
            )
            latest_movie = kwargs['latest_movie']

            director = Directors.objects.create(name=name, date_of_birth=date_of_birth, latest_movie=latest_movie)

            self.stdout.write(self.style.SUCCESS(f'Successfully added {name} to the database!'))
        elif kwargs['write']:
            directors = Directors.objects.all()
            for i, director in enumerate(directors):
                self.stdout.write(
                    f'{i+1}. {director.name} born on {director.date_of_birth}. The latest movie he/she directed is called {director.latest_movie}'
                )
        elif kwargs['delete']:
            record_number = kwargs['delete'] - 1
            director_to_delete = Directors.objects.all()[record_number]
            director_to_delete.delete()
            self.stdout.write(self.style.SUCCESS(f'Successfully deleted director no. {record_number} from database!'))
        elif kwargs['movies']:
            if kwargs['movies'] < 1 or kwargs['movies'] > Directors.objects.count():
                self.stdout.write(self.style.ERROR('Given number doesnt match any Director in the DataBase!'))
            else:
                selected = kwargs['movies'] - 1
                director_selected = Directors.objects.all()[selected]
                movies = director_selected.movies.all()
                if movies.count() == 0:
                    self.stdout.write(f'There are no movies matching selected director in the Database :(')
                else:
                    self.stdout.write(f'Movies directed by {director_selected.name} in the DataBase:')
                    for i, movie in enumerate(movies):
                        self.stdout.write(
                            f'{i+1}. "{movie.title}" released on {movie.premiere_date} starring {movie.lead_actor} in lead role. It has won {movie.academy_awards} Academy Awards.'
                        )

        else:
            self.stdout.write(
                self.style.ERROR('You need to present at least one valid main flag! Type --help to get more info')
            )
