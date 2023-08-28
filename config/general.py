import os
from pathlib import Path


class ProjectPaths:
    CONFIG = Path(__file__).parent
    ROOT = CONFIG.parent
    LOGS = os.path.join(ROOT, 'logs')