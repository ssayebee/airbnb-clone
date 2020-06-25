from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):

    help = "this command create superuser"

    def handle(self, *args, **options):
        admin = User.objects.get_or_none(username="ebadmin")
        if not admin:
            User.objects.create_superuser("ebadmin", "ssayebee@ssayebee.co", "123456")
            self.stdout.write(self.style.SUCCESS(f"Superuser Created"))
        self.stdout.write(self.style.SUCCESS(f"Superuser Exists"))
