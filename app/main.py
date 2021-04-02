from services import waypoint_scenarios, quest_scenarios
from services.build_campaign import Campaign
from log_setup import log

if __name__ == "__main__":
    number_waypoint_scenario = waypoint_scenarios.get_number_of_waypoint_scenarios()
    log.info(f"We have {number_waypoint_scenario} waypoint available")
    number_quests_available = quest_scenarios.get_number_of_quest_scenarios()
    log.info(f"We have {number_quests_available} quests available")

    random_waypoint_scenario = waypoint_scenarios.get_random_scenario(10)
    random_quest = quest_scenarios.get_random_scenario(1)
    campaign = Campaign()
    campaign.build_campaign(
        waypoint_list=random_waypoint_scenario, quest_list=random_quest
    )
