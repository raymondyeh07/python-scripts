import logging

logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)
logger.addHandler(ch)
logger.warning('attention')
