import os

from src.common.constants import *
from src.util.json_util import json_to_dict


class JsonDiverConfiguration:
    def __init__(self, driver_type):
        self._driver_type = driver_type
        self._configuration_dict = json_to_dict(self._driver_type.value)

    @property
    def driver_type(self):
        return self._driver_type

    def get_hub_url(self):
        return os.environ.get('HUB_URL', 'http://localhost:4444')

    def get_capabilities(self):
        return self._configuration_dict[DRIVER_CAPABILITIES_KEY]

    def get_timeout(self):
        return self._configuration_dict[DRIVER_TIMEOUT_KEY]
