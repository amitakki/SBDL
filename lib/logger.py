class Log4j(object):
    def __init__(self, spark):
        log4j = spark._jvm.org.apache.log4j
        self.logger = log4j.LogManager.getLogger("sbdl")

    def warn(self, message):
        return self.logger.warn(message)

    def info(self, message):
        return self.logger.info(message)

    def error(self, message):
        return self.logger.error(message)

    def debug(self, message):
        return self.logger.debug(message)
