from django.core.management.base import BaseCommand, CommandParser
from core.models import Movies, Directors, Actors
from datetime import datetime

class Command(BaseCommand):
    help = 'Add a new Actor figure to the DataBase. In order to do that you shall pass --add flag followed by --name, --date_of_birth, --latest_movie'

    def add_arguments(self, parser):
        parser.add_argument('--write', action='store_true', help = "Flag --write is necessary to write out the contents of database")
        parser.add_argument('--add', action='store_true', help = 'Flag --add is necessary to add an actor to the DB')
        parser.add_argument('--delete', type=int, help = 'Use this flag to delete a record from selected table, follow it with number >0 that indicates which record you want to get rid of')
        parser.add_argument('--movies', type=int, help = f'This flag will query through DB and write out info about movies starring selected actor in lead role. To select an actor write a positive number after the flag ')
        parser.add_argument('--name', type=str, help='Full name of an actor, prefferably using Capital letters and good name format')
        parser.add_argument('--date_of_birth', type=str, help='date of birth of an actor in format YYYY/MM/DD')
        parser.add_argument('--latest_movie', type=str, help='Title of a latest movie which starred given actor')
        

    def handle(self, *args, **kwargs):
        if kwargs['add']:
            name = kwargs['name']
            date_of_birth = datetime.strptime(kwargs['date_of_birth'], '%Y-%m-%d').date() if kwargs['date_of_birth'] else None
            latest_movie = kwargs['latest_movie']

            actor = Actors.objects.create(
                name = name,
                date_of_birth = date_of_birth,
                latest_movie = latest_movie
            )

            self.stdout.write(self.style.SUCCESS(f"Successfully added {name} to the database!"))
        elif kwargs['write']:
            actors = Actors.objects.all()
            for i, actor in enumerate(actors):
                self.stdout.write(f'{i+1}. {actor.name} born on {actor.date_of_birth}. The latest movie he/she starred in is called "{actor.latest_movie}"')
        elif kwargs['delete']:
            record_number = kwargs['delete'] - 1
            actor_to_delete = Actors.objects.all()[record_number]
            actor_to_delete.delete()
            self.stdout.write(self.style.SUCCESS(f"Successfully deleted actor no. {record_number} from database!"))
        elif kwargs['movies']:
            if kwargs['movies']<1 or kwargs['movies'] > Actors.objects.count():
                self.stdout.write(self.style.ERROR("Given number doesnt match any Actor in the DataBase!"))
            else:
                selected = kwargs['movies'] - 1
                actor_selected = Actors.objects.all()[selected]
                movies = actor_selected.movies.all()
                if movies.count()==0: self.stdout.write(f"There are no movies matching selected actor in the Database :(")
                else:
                    self.stdout.write(f"Movies staring {actor_selected.name} as a lead role in the DataBase:")
                    for i, movie in enumerate(movies):
                        self.stdout.write(f'{i+1}. "{movie.title}" released on {movie.premiere_date} directed by {movie.director.name} and has won {movie.academy_awards} Academy Awards.')
        else: 
            self.stdout.write(self.style.ERROR("You need to present at least one valid main flag! Type --help to get more info"))