import json

import yaml


def get_config() -> json:
    # read file
    with open(f"config/config.yml", "r") as config_file:
        config_data = yaml.load(config_file, Loader=yaml.FullLoader)
    return config_data
