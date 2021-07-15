import logging

LOGGER = logging.getLogger()  # Tạo instance logging
LOG_LEVEL = logging.DEBUG  # Level để in log


def config_file() -> None:
    """
    Cấu hình logger để in lên console
    :return: None
    """
    console_logger = logging.FileHandler('FILE_LOG.log')
    LOGGER.addHandler(console_logger)


def main():
    try:
        open('/path/to/does/not/exist.txt', 'rb')
    except Exception as e:
        LOGGER.error('Failed to open file', exc_info=False)


if __name__ == '__main__':
    config_file()
    LOGGER.setLevel(LOG_LEVEL)
    main()
