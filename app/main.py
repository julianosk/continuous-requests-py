import os
import time
import requests

URL = os.environ['URL']
INTERVAL = int(os.environ['INTERVAL'])

print('URL = {}'.format(URL))
print('INTERVAL = {}'.format(INTERVAL))

while True:
  try:
    print(requests.get(URL, timeout=INTERVAL))
  except:
    print("Error requesting {}".format(URL))
  time.sleep(INTERVAL)