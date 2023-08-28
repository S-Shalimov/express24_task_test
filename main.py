import logging.config


def main():
    logging.config.fileConfig("logging_config.ini", disable_existing_loggers=False)

if __name__ == "__main__":
    main()