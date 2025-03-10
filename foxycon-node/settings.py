import json
import logging.config
import os

from dotenv import dotenv_values
from types import SimpleNamespace

config_file_path = os.path.join(os.path.dirname(__file__), "logging_config.json")

with open(config_file_path, "r") as file:
    configs = json.load(file)
    logging.config.dictConfig(configs)

logger = logging.getLogger(__name__)


TEST = True


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


logger.info(parameters_col)
