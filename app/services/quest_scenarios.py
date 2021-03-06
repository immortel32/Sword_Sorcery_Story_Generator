import json
import os
import random
from typing import List

import yaml

from log_setup import log

# -----------------------------------------------
from models.quest import Quest
from models.waypoint import Waypoint
from services import configuration_reader

cfg = configuration_reader.get_config()
quest_directory_path = f"{cfg['data_dir']}{cfg['language']}/{cfg['quest_dir']}"


# -----------------------------------------------


def _list_of_files() -> List[str]:
    """
    Return the list of waypoint story files
    :return:
    """

    file_list = (f for f in os.listdir(quest_directory_path) if f.endswith("." + "yml"))
    quest_list_file = []
    for file in file_list:
        if not file.startswith("_"):
            quest_list_file.append(file)
    return quest_list_file


# -----------------------------------------------


def get_number_of_quest_scenarios() -> int:
    """
    Return the number of existing waypoint stories
    :return:
    """
    quest_list_file = _list_of_files()
    return len(quest_list_file)


# -----------------------------------------------


def load_scenario(file_name: str) -> Waypoint:
    """
    Create an object Waypoint from a Scenario file
    :param file_name:
    :return:
    """

    # read file
    with open(f"{quest_directory_path}/{file_name}", "r") as scenario_file:
        scenario_data = yaml.load(scenario_file, Loader=yaml.FullLoader)
    quest = Quest()
    quest.build_from_json(scenario_data)

    return quest


# -----------------------------------------------


def get_random_scenario(number_random_scenario_required: int) -> List[Waypoint]:
    """
    Return the number of scenario randomly selected from the existing waypoint
    :param number_random_scenario_required:
    :return: List[Waypoint]
    """
    max_available_scenario = get_number_of_quest_scenarios()
    if max_available_scenario < number_random_scenario_required:
        log.info(
            f"There are only {max_available_scenario} scenario available, "
            f"{number_random_scenario_required} has been required"
        )
        number_random_scenario_required = max_available_scenario
    list_scenario = []
    selected_scenarios = random.sample(
        _list_of_files(), number_random_scenario_required
    )
    log.info(f"Will generate scenarios for {selected_scenarios}")
    for scenario in selected_scenarios:
        list_scenario.append(load_scenario(scenario))
    return list_scenario
