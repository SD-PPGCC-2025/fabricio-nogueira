import logging
import sys

root = logging.getLogger()
root.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s:[%(levelname)s]: %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)