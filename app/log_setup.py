import logging
from logging.handlers import TimedRotatingFileHandler

log = logging.getLogger()
handler = TimedRotatingFileHandler("logs/ss_story_generator.log", "midnight", 1, 7)
fmt = "%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s"
formatter = logging.Formatter(fmt=fmt, datefmt="%m/%d/%Y %H:%M:%S")

handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)

# console = logging.StreamHandler()
# console.setFormatter(formatter)
# console.setLevel(logging.INFO)
# logger.addHandler(console)
log.addHandler(handler)
log.setLevel(logging.INFO)
