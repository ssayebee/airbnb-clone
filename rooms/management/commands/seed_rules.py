from django.core.management.base import BaseCommand
from rooms.models import HouseRule


class Command(BaseCommand):

    help = "this command create house rules"

    def handle(self, *args, **options):
        house_rules = [
            "Don't Smoking",
            "Catering prohibited",
            "Do not go out after 12:00",
        ]
        for h in house_rules:
            HouseRule.objects.create(name=h)
        self.stdout.write(
            self.style.SUCCESS(f"{len(house_rules)} house rules created!")
        )
