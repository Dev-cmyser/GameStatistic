import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import Event, SubUser, Version


def main_graf(request):

    return render(request, "grafs/graf.html")

def logarifm(request):

    return render(request, "grafs/graf-logarifmic.html")

def _get_versions() -> list:
    versions = Version.objects.all()
    versions_list = []
    for i in versions:
        versions_list.append(i.versionIdentifier)

    versions_list = sorted(versions_list)
    return versions_list


def _get_period_versions() -> dict:
    events = Event.objects.all()
    versions = Version.objects.all()
    versions_dict = {}

    for i in versions:
        versions_dict[i.versionIdentifier] = 0

    for j in versions:
        for i in events:
            if j.startDate <= i.date <= j.endDate:
                versions_dict[j.versionIdentifier] += 1
    return versions_dict


def _get_events_to_version() -> dict:
    events = Event.objects.all()
    versions = Version.objects.all()
    events_to_version = {}
    ev_from_egor = [
        "dialogue_marya_close_0",
        "merge_marya",
        "dialogue_marya_close_1",
        "merge_stebel",
        "dialogue_marya_close_2",
        "merge_bloom_tree",
        "dialogue_marya_close_3",
        "quest_done_0",
        "level_up_2",
        "quest_open_1",
        "2_apple_harvested",
        "dialogue_marya_close_4",
        "dialogue_marya_close_5",
        "quest_done_1",
        "dialogue_marya_close_6",
        "dialogue_marya_close_7",
        "dialogue_marya_close_8",
        "dialogue_marya_close_10",
        "dialogue_marya_close_11",
        "dialogue_marya_close_12",
        "dialogue_marya_close_13",
        "dialogue_marya_close_14",
        "dialogue_marya_close_15",
        "dialogue_marya_close_16",
        "dialogue_marya_close_17",
        "dialogue_marya_close_18",
        "dialogue_marya_close_19",
        "dialogue_marya_close_20",
        "open_map_2",
        "quest_open_2",
        "quest_open_17",
        "dialogue_mc_close_0",
        "dialogue_cat_close_0",
        "first_click_in_root",
        "second_click_in_root",
        "dialogue_cat_close_1",
        "first_click_in_chest",
        "first_click_in_chest_open",
        "quest_done_2",
        "level_up_3",
        "dialogue_cat_close_1",
        "open_map_3",
        "dialogue_cat_close_8",
        "quest_done_17",
        "quest_done_2",
        "quest_open_5",
        "level_up_4",
        "open_map_4",
        "open_map_5",
        "dialogue_cat_close_2",
        "dialogue_mc_close_7",
        "dialogue_cat_close_5",
        "dialogue_cat_close_6",
        "dialogue_cat_close_3",
        "dialogue_mc_close_1",
        "quest_done_5",
        "quest_open_7",
        "quest_open_8",
        "quest_open_3",
        "quest_open_4",
        "dialogue_cat_close_4",
        "quest_open_6",
        "quest_done_3",
        "quest_open_9",
        "dialogue_mc_close_6",
        "quest_done_7",
        "dialogue_cat_close_5",
        "dialogue_cat_close_6",
        "dialogue_cat_close_7",
        "dialogue_cat_close_8",
        "dialogue_cat_close_9",
        "dialogue_cat_close_10",
        "dialogue_cat_close_11",
        "dialogue_cat_close_12",
        "dialogue_cat_close_13",
        "dialogue_cat_close_14",
        "dialogue_cat_close_15",
        "quest_open_10",
        "quest_done_9",
        "quest_open_14",
        "quest_open_16",
        "quest_open_15",
        "level_up_5",
        "quest_done_16",
        "quest_done_15",
        "quest_done_14",
        "quest_done_13",
        "quest_open_13",
        "quest_open_12",
        "quest_done_12",
        "quest_done_11",
        "quest_open_11",
        "quest_done_10",
        "quest_open_18",
        "quest_open_19",
        "quest_open_20",
        "quest_open_21",
        "quest_open_22",
        "quest_open_23",
        "quest_done_18",
        "quest_done_19",
        "quest_done_20",
        "quest_done_21",
        "quest_done_22",
        "quest_done_23",
        "quest_done_4",
        "level_up_6",
        "level_up_7",
        "level_up_8",
        "level_up_9",
        "level_up_10",
        "open_map_6",
        "open_map_7",
        "open_map_8",
        "open_map_9",
        "open_map_10",
        "quest_done_6",
        "first-drop-apples",
        "first-exchange",
        "first-key-collect",
        "first-cutting-of-the-root",
        "first-merge-logs",
        "second-cutting-of-the-root",
        "first-delete-root",
        "first-open-chestS",
        "second-open-chestS",
        "dialogue_mi_close_0",
        "dialogue_mi_close_1",
        "dialogue_mi_close_2",
        "dialogue_mi_close_3",
        "dialogue_mi_close_4",
        "dialogue_mi_close_5",
        "dialogue_mi_close_6",
        "spawn_fisherwoman",
        "spawn_fourth_character",
        "learn_modal_close",
        "first_items_spawn",
        "spawn_ivan"
    ]
    
    for j in versions:
        for i in events:
            if j.versionIdentifier in events_to_version:
                pass
            else:
                events_to_version[j.versionIdentifier] = {}
            # print(events_to_version[j.versionIdentifier])
            # print('\n\n\n\n\n\n\n\n\n')
            # print(j.startDate, 'j.startDate')
            # print(i.date, 'i.date')
            # print(j.endDate, 'j.endDate')
            if j.startDate <= i.date <= j.endDate:
                if i.eventName in ev_from_egor:
                    try:
                        events_to_version[j.versionIdentifier][i.eventName] += 1
                    except KeyError:
                        events_to_version[j.versionIdentifier][i.eventName] = 0
                
    return events_to_version


def get_data(request):
    events_to_version = _get_events_to_version()
    v_dict_count = _get_period_versions()
    versions_list = _get_versions()
    data = {
        "versions": versions_list,
        "v_dict_count": v_dict_count,
        "events_to_version": events_to_version,
    }
    response = JsonResponse(data, safe=False)

    return response
