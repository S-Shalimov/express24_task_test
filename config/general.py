import os
from pathlib import Path


class ProjectPaths:
    CONFIG = Path(__file__).parent
    ROOT = CONFIG.parent
    LOGS = os.path.join(ROOT, 'logs')
    BASE_LOG_CONFIG = os.path.join(LOGS, "base_logging_config.ini")