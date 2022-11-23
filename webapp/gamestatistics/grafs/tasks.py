from gamestatistics.celery import app
import requests
import json

from datetime import datetime

from grafs.models import Event, SubUser, Version


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

def _get_all_data() ->  None:
    print("version")
    get_gata_versions()
    print("allusers")
    get_gata_allusers()
    print("events")
    get_gata_events()


def _get_dict():
    with open("data/data_events.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def _create_all_data() -> None:
    data_event = _get_dict()
    
    for d_event in data_event:
        defaults_event = {
        'platform': d_event['platform'],
        'deviceType': d_event['deviceType'],
        'eventName': d_event['eventName'],
        'language': d_event['language'],
        'referrer': d_event['referrer'],
        'localTime': d_event['localTime'],
        'date': d_event['date'], 
        'loadTime': 1 if d_event['loadTime'] == '' else d_event['loadTime'],
        'timeFromStart': d_event['timeFromStart']
        }
        obj_event, created_event = Event.objects.get_or_create(
        sub_id=d_event['id'],
        defaults=defaults_event,
        )
        d_version = d_event['version']
        defaults_versions = {
            'versionIdentifier' : d_version['versionIdentifier'],
            'platform' : d_version['platform'],
            'startTime' : d_version['startTime'],
            'startDate' : d_version['startDate'],
            'startDateLong' : d_version['startDateLong'],
            'endTime' : d_version['endTime'],
            'endDate' : d_version['endDate'],
            'endDateLong' : d_version['endDateLong']
        }
        obj_version, created_version = Version.objects.get_or_create(
            sub_id = d_version['id'],
            defaults=defaults_versions,
            
        )
        d_user = d_event['userEntity']
        defaults_subuser = {
            'platformUserId' : d_user['platformUserId'] or -1,
            'sessionCounter' : d_user['sessionCounter']or -1,
            'playTime' : d_user['playTime'] or -1,
            'active' : d_user['active'],
            'lastActivity' : d_user['lastActivity'] or -1,
            'referer' : d_user['referer'],
            'registrationDate' : d_user['registrationDate'],
            'adsCounter' : d_user['adsCounter'] or -1,
            'platform' : d_user['platform'],
            'deviseType' : d_user['deviseType'],
        }
        obj_user, created_user = SubUser.objects.get_or_create(
            sub_id = d_user['id'],
            defaults=defaults_subuser,  
        )
        
        obj_user.event.add(obj_event)

@app.task
def repeat_order_make():
    print("получаем данные")
    _get_all_data()
    print("\n\n\nStarting to  create_all_data!\n\n\n\n\n\n\n\n\n\n")
    _create_all_data()
    print("\n\n\nFinish! to  create_all_data!\n\n\n\n\n\n\n\n\n\n")

 
