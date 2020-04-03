from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):

    help = "this command create facilites"

    def handle(self, *args, **options):
        facilites = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for f in facilites:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilites)} facilities created!"))
