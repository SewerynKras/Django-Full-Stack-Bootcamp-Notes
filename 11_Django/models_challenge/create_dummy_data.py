import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "models_challenge.settings")

import django
django.setup()

from users.models import User
from faker import Faker

faker = Faker()

def create_dummy_data(num=5):
    for i in range(num):
        first_name = faker.first_name()
        last_name = faker.last_name()
        email = faker.email()

        user = User.objects.get_or_create(first_name=first_name,
                                          last_name=last_name,
                                          email=email)

if __name__ == "__main__":
    create_dummy_data(20)
