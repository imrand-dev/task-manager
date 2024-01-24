from django.core.management.base import BaseCommand
from django.db import transaction

from accounts.services.users import UserService


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with transaction.atomic():
            user_service = UserService()

            superuser = user_service.create_superuser(
                email="imranxdoe@gmail.com",
                password1="123456",
                password2="123456",
                first_name="Imran",
                last_name="Potter",
            )

            self.stdout.write("Super user has been created.")