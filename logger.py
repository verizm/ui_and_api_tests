import sys
import logging

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)
handler = logging.StreamHandler(stream=sys.stdout)
LOGGER.addHandler(handler)


#ДЛЯ 1 коммита в new branch