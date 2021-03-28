import json
import os
import random
from typing import List
from log_setup import log

# -----------------------------------------------
from models.waypoint import Waypoint
from services import configuration_reader

cfg = configuration_reader.get_config()
waypoint_directory_path = f"{cfg['data_dir']}{cfg['language']}/{cfg['waypoint_dir']}"


# -----------------------------------------------

def _list_of_files() -> List[str]:
    """
    Return the list of waypoint story files
    :return:
    """

    file_list = (f for f in os.listdir(waypoint_directory_path) if f.endswith('.' + "json"))
    waypoint_list_file = []
    for file in file_list:
        if not file.startswith("_"):
            waypoint_list_file.append(file)
    return waypoint_list_file


# -----------------------------------------------

def get_number_of_waypoint_scenarios() -> int:
    """
    Return the number of existing waypoint stories
    :return:
    """
    waypoint_list_file = _list_of_files()
    return len(waypoint_list_file)


# -----------------------------------------------

def load_scenario(file_name: str) -> Waypoint:
    """
    Create an object Waypoint from a Scenario file
    :param file_name:
    :return:
    """

    # read file
    with open(f"{waypoint_directory_path}/{file_name}", 'r') as scenario_file:
        scenario_data = scenario_file.read()
    waypoint = Waypoint()
    waypoint.build_from_json(json.loads(scenario_data))

    return waypoint


# -----------------------------------------------

def get_random_scenario(number_random_scenario_required: int) -> List[Waypoint]:
    """
    Return the number of scenario randomly selected from the existing waypoint
    :param number_random_scenario_required:
    :return: List[Waypoint]
    """
    max_available_scenario = get_number_of_waypoint_scenarios()
    if max_available_scenario < number_random_scenario_required:
        log.info(f"There are only {max_available_scenario} scenario available, {number_random_scenario_required} has been required")
        number_random_scenario_required = max_available_scenario
    list_scenario = []
    selected_scenarios = random.sample(_list_of_files(), number_random_scenario_required)
    log.info(f"Will generate scenarios for {selected_scenarios}")
    for scenario in selected_scenarios:
        list_scenario.append(load_scenario(scenario))
    return list_scenario
