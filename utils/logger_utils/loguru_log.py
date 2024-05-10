import loguru


class Logger:
    def __init__(self, log_file, log_level='INFO'):
        self.log_file = log_file
        self.log_level = log_level

        # 配置loguru
        loguru.logger.remove()
        loguru.logger.add(self.log_file, level=self.log_level)

    def info(self, message):
        loguru.logger.info(message)

    def debug(self, message):
        loguru.logger.debug(message)

    def warning(self, message):
        loguru.logger.warning(message)

    def error(self, message):
        loguru.logger.error(message)

    def critical(self, message):
        loguru.logger.critical(message)
