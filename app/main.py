from services import waypoint_scenarios
from services.build_quest import Quest
from log_setup import log

if __name__ == "__main__":
    number_waypoint_scenario = waypoint_scenarios.get_number_of_waypoint_scenarios()
    log.info(f"We have {number_waypoint_scenario} waypoint scenario")
    random_waypoint_scenario = waypoint_scenarios.get_random_scenario(10)
    quest = Quest()
    quest.build_quest(waypoint_list=random_waypoint_scenario)
