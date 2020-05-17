from django.core.management.base import BaseCommand
from app.models import *
class Command(BaseCommand):
    help = 'This command Saves Data of Member'

    def add_arguments(self, parser):
        parser.add_argument('id', type=str, help='Indicates the id of the member to be created')
        parser.add_argument('real_name', type=str, help='Indicates the real_name of the member to be created', nargs=2)
        parser.add_argument('tz', type=str, help='Indicates the timezone of the member to be created')

    def handle(self, *args, **kwargs):
        id = kwargs['id']
        real_name = kwargs['real_name']
        tz = kwargs['tz']
        name = ''
        for i in real_name:
            name += i
            name += ' '
        print(name)

        try:
            m = member(id = id, real_name = name, tz = tz)
            m.save()
            print(m)
        except:
            raise CommandError('Unable to save')
        self.stdout.write("Member Data saved!")