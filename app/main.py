import os
import time
import requests

URL = os.environ['URL']
INTERVAL = int(os.environ['INTERVAL'])

print('URL = {}'.format(URL))
print('INTERVAL = {}'.format(INTERVAL))

while True:
  print(requests.get(URL))
  time.sleep(INTERVAL)