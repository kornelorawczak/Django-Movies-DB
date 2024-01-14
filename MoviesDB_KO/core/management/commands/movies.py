from django.core.management.base import BaseCommand, CommandParser
from core.models import Movies, Directors, Actors
from datetime import datetime

class Command(BaseCommand):
    help = 'Use --add followed by --title, --premiere_date, --director, --category, --lead_actor, --academy_awards to add a new Movie to the database. \n Use --write to write out all the \
        movies that currently are in database'

    def add_arguments(self, parser):
        parser.add_argument('--write', action='store_true', help = "Flag --write is necessary to write the contents of database")
        parser.add_argument('--add', action='store_true', help = 'Flag --add is necessary to add a movie to the DB')
        parser.add_argument('--delete', type=int, help = 'Use this flag to delete a record from selected table, follow it with number >0 that indicates which record you want to get rid of')
        parser.add_argument('--title', type=str, help='Title of a movie')
        parser.add_argument('--premiere_date', type=str, help='Premiere_date of a movie in format YYYY/MM/DD')
        parser.add_argument('--director', type=str, help=f'Full name of a director: {[dir.name for dir in Directors.objects.all()]}')
        parser.add_argument('--category', type=str, help='Category of a movie')
        parser.add_argument('--lead_actor', type=str, help=f'Full name of lead actor: {[actor.name for actor in Actors.objects.all()]}')
        parser.add_argument('--academy_awards', type=int, help='Number of oscars won by the movie. Pass the number 0-11')

    def handle(self, *args, **kwargs):
        if kwargs['add']:
            title = kwargs['title']
            premiere_date = datetime.strptime(kwargs['premiere_date'], '%Y-%m-%d').date() if kwargs['premiere_date'] else None
            director_given = kwargs['director']
            category = kwargs['category']
            lead_actor_given = kwargs['lead_actor']
            academy_awards = kwargs['academy_awards']

            director, created = Directors.objects.get_or_create(name = director_given)

            lead_actor, created = Actors.objects.get_or_create(name = lead_actor_given)

            movie = Movies.objects.create(
                title = title,
                premiere_date = premiere_date,
                director = director,
                category = category,
                lead_actor = lead_actor,
                academy_awards = academy_awards
            )

            self.stdout.write(self.style.SUCCESS(f'Successfully added movie "{title}" to the database!'))
        elif kwargs['write']:
            movies = Movies.objects.all()
            for i, movie in enumerate(movies):
                self.stdout.write(f'{i+1}. "{movie.title}" ({movie.category}) premiered {movie.premiere_date}. It was directed by {movie.director} and starred {movie.lead_actor}. It won {movie.academy_awards} academy awards.')
        elif kwargs['delete']:
            record_number = kwargs['delete'] - 1
            movie_to_delete = Movies.objects.all()[record_number]
            movie_to_delete.delete()
            self.stdout.write(self.style.SUCCESS(f"Successfully deleted movie no. {record_number} from database!"))
        else: 
            self.stdout.write(self.style.ERROR("You need to present at least one valid main flag! Type --help to get more info"))