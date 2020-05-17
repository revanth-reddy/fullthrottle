from django.core.management.base import BaseCommand
from app.models import *
class Command(BaseCommand):
    help = 'This command Saves Activity Period Data of Member'

    def add_arguments(self, parser):
        parser.add_argument('id', type=str, help='Indicates the id of the member')
        parser.add_argument('start_time', type=str, help='Indicates the start_time of the Activity Period to be created', nargs=4)
        parser.add_argument('end_time', type=str, help='Indicates the timezone of the Activity Period to be created', nargs=4)

    def handle(self, *args, **kwargs):
        id = kwargs['id']
        start_time = kwargs['start_time']
        end_time = kwargs['end_time']
        st = ''
        et = ''
        for i in start_time:
            st += i
            st += ' '
        
        for i in end_time:
            et += i
            et += ' '
        
        # print(st)
        # print(et)
        m = member.objects.get(id = id)
        try:
            a = activity(member = m, start_time = st, end_time = et)
            a.save()
            print(a)
        except m.DoesNotExist:
            raise CommandError('Unable to save')
        self.stdout.write("Data Saved!")