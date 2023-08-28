import logging.config

from config.general import ProjectPaths


def main():
    logging.config.fileConfig(ProjectPaths.BASE_LOG_CONFIG, disable_existing_loggers=False)

if __name__ == "__main__":
    main()