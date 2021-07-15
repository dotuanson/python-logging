import logging

NEW_FORMAT = '[%(asctime)s] - [%(levelname)s] - %(message)s'  # Format message log
FILE_LOG = r'..\logfile.log'  # File để lưu logs
LOGGER = logging.getLogger()  # Tạo instance logging
LOG_LEVEL = logging.DEBUG  # Level để in log


def config_file() -> None:
    """
    Cấu hình logger để in ra file
    :return: None
    """
    file_logger = logging.FileHandler(FILE_LOG)
    file_logger_format = logging.Formatter(NEW_FORMAT)
    file_logger.setFormatter(file_logger_format)
    LOGGER.addHandler(file_logger)


def config_console() -> None:
    """
    Cấu hình logger để in lên console
    :return: None
    """
    console_logger = logging.StreamHandler()
    console_logger_format = logging.Formatter(NEW_FORMAT)
    console_logger.setFormatter(console_logger_format)
    LOGGER.addHandler(console_logger)


if __name__ == '__main__':
    LOGGER.setLevel(LOG_LEVEL)  # Hiển thị các log từ DEBUG -> CRITICAL
    config_file()
    config_console()

    # Testingggggg!!!!!!
    LOGGER.debug("This is a debug message!")
    LOGGER.info("This is an info message!")
    LOGGER.warning("This is a warning message!")
