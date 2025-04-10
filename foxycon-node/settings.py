import json
import logging.config
import os

from dotenv import dotenv_values
from types import SimpleNamespace

config_file_path = os.path.join(os.path.dirname(__file__), "logging_config.json")




TEST = False


def get_parameters():
    config = dotenv_values(".env")
    parameters = {}

    for key, value in config.items():
        parts = key.split("_")
        if TEST:
            if parts[0] == "TEST":
                parameters["_".join(parts[1:])] = value
        else:
            if parts[0] != "TEST":
                parameters["_".join(parts)] = value

    return SimpleNamespace(**parameters)


parameters_col = get_parameters()



