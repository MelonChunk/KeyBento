import os
from api.config import ProdSettings, DebugSettings


def get_settings():

    if os.environ.get("ENV") == "PROD":
        return ProdSettings()

    return DebugSettings()
