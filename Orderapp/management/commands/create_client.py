from django.core.management.base import BaseCommand

from Orderapp.models import ClientModel


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        client = ClientModel(name='John', email='john@example.com', phone='+1(202)1234567', address='Washington, DC', reg_date='2022-05-01')
        client.save()
        self.stdout.write(f'{client} added')

        client = ClientModel(name='Emily', email='emily@example.com', phone='+1(212)7654321', address='New York, NY', reg_date='2023-07-15')
        client.save()
        self.stdout.write(f'{client} added')

        client = ClientModel(name='Robert', email='robert@example.com', phone='+1(305)9876543', address='Miami, FL', reg_date='2024-02-20')
        client.save()
        self.stdout.write(f'{client} added')
