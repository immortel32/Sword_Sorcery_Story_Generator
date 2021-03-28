import json


def get_config() -> json:
    # read file
    with open(f"config/config.json", 'r') as config_file_file:
        config_data = config_file_file.read()
    return json.loads(config_data)
