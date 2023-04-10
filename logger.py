import sys
import logging

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)
handler = logging.StreamHandler(stream=sys.stdout)
LOGGER.addHandler(handler)

# commit from master

