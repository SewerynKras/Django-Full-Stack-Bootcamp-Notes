import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_project.settings")

import django
django.setup()

from random import choice
from first_app.models import Webpage, Topic, AccessRecord
from faker import Faker

faker = Faker()

TOPICS = ["Social Network", "Business", "News", "Reviews", "Game"]


def getTopic():
    random_topic = choice(TOPICS)
    topic = Topic.objects.get_or_create(topic_name=random_topic)[0]
    topic.save()
    return topic


def create_dummy_data(num=5):
    for i in range(num):
        topic = getTopic()
        random_url = faker.url()
        random_date = faker.date()
        random_name = faker.company()

        webpage = Webpage.objects.get_or_create(topic=topic,
                                                url=random_url,
                                                name=random_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=webpage,
                                                     date=random_date)[0]


if __name__ == "__main__":
    create_dummy_data(20)
