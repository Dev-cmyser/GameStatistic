import requests
import json

from datetime import datetime

from grafs.models import Event, SubUser, Version
from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

   

    def handle(self, *args, **options):
        pass

# datetime_str = '09/19/18 13:55:26'

# datetime_object = datetime.strptime(datetime_str, '%m/%d/%y %H:%M:%S')


def get_gata_versions():
    r = requests.get("https://codovstvo.ru/back/data/allversions")
    text = r.content
    my_json = text.decode("utf8").replace("'", '"')
    with open("data/data_version.json", "w") as file:
        file.write(my_json)


def get_gata_allusers():
    r = requests.get("https://codovstvo.ru/back/data/allusers")
    text = r.content
    my_json = text.decode("utf8").replace("'", '"')
    with open("data/data_users.json", "w") as file:
        file.write(my_json)


def get_gata_events():
    print("now req")
    r = requests.get("https://codovstvo.ru/back/data/allevents")
    text = r.content
    print("теперь файл")
    my_json = text.decode("utf8").replace("'", '"')
    with open("data/data_events.json", "w") as file:
        file.write(my_json)


def _get_dict():
    with open("data/data_events.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def create_all_data() -> None:
    data_event = _get_dict()
    count = 0
    for d_event in data_event:
        count += 1
        # obj_event, created_event = Event.objects.update_or_create(
        # sub_id=d_event['id'],
        # platform=d_event['platform'],
        # deviceType=d_event['deviceType'],
        # eventName=d_event['eventName'],
        # language=d_event['language'],
        # referrer=d_event['referrer'],
        # localTime=d_event['localTime'],
        # date=d_event['date'], 
        # loadTime= 1 if d_event['loadTime'] == '' else d_event['loadTime'],
        # timeFromStart=d_event['timeFromStart']
        # )
        # d_version = d_event['version']
        # obj_version, created_version = Version.objects.update_or_create(
        #     sub_id = d_version['id'],
        #     versionIdentifier = d_version['versionIdentifier'],
        #     platform = d_version['platform'],
        #     startTime = d_version['startTime'],
        #     startDate = d_version['startDate'],
        #     startDateLong = d_version['startDateLong'],
        #     endTime = d_version['endTime'] ,
        #     endDate = d_version['endDate'] ,
        #     endDateLong = d_version['endDateLong']
        # )
        # d_user = d_event['userEntity']
        # obj_user, created_user = SubUser.objects.update_or_create(
        #     sub_id = d_user['id'],
        #     platformUserId = int(d_user['platformUserId']),
        #     sessionCounter = d_user['sessionCounter'],
        #     playTime = d_user['playTime'],
        #     active = d_user['active'],
        #     lastActivity = d_user['lastActivity'],
        #     referer = d_user['referer'],
        #     registrationDate = d_user['registrationDate'],
        #     adsCounter = d_user['adsCounter'],
        #     platform = d_user['platform'],
        #     deviseType = d_user['deviseType'],
        #     event = obj_event
            
        # )
    print(count)

create_all_data()
# get_gata_allusers()
# get_gata_versions()
# get_dict()
# get_gata_events()
