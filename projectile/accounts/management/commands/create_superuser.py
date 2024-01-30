import getpass

from django.core.management.base import BaseCommand
from django.db import transaction

from accounts.services.users import UserService


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with transaction.atomic():
            email = self.get_input_data(field="Email")
            password1 = self.get_input_data(field="Password", is_password=True)
            password2 = self.get_input_data(field="Confirm Password", is_password=True)

            if password1 != password2:
                raise ValueError("Passwords do not match.")

            first_name = self.get_input_data(field="First name")
            last_name = self.get_input_data(field="Last name")

            user_service = UserService()
            superuser = user_service.create_superuser(
                email=email,
                password1=password1,
                password2=password2,
                first_name=first_name,
                last_name=last_name,
            )

            self.stdout.write(self.style.SUCCESS("Superuser created successfully."))

    def get_input_data(self, field, is_password=False):
        prompt = f"{field}: "

        if is_password:
            input_value = getpass.getpass(prompt)
        else:
            input_value = input(prompt)
        
        return input_value