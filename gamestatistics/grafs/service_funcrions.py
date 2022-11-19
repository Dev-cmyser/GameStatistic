import requests
import json

from datetime import datetime

from .models import Event, SubUser, Version

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
    data = _get_dict()
    print(data[0])


# get_gata_allusers()
# get_gata_versions()
# get_dict()
# get_gata_events()
