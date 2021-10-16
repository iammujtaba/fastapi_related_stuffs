import os
import importlib

ENVIRONMENT_VARIABLE = "FASTAPI_SETTINGS_MODULE"

class LazySettings:
    def __init__(self):
        self.env = os.environ.get(ENVIRONMENT_VARIABLE,"main.local_settings")

    def get_settings(self):
        return importlib.import_module(self.env)

settings = LazySettings().get_settings()
