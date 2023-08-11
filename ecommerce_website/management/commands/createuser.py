from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create a regular user'

    def add_arguments(self, parser):
        parser.add_argument('--username', required=True, help='Username for the new user')
        parser.add_argument('--email', required=True, help='Email for the new user')
        parser.add_argument('--password', required=True, help='Password for the new user')

    def handle(self, *args, **options):
        username = options['username']
        email = options['email']
        password = options['password']

        user = User.objects.create_user(username=username, email=email, password=password)
        self.stdout.write(self.style.SUCCESS(f'Successfully created user: {user.username}'))
