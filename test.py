import httpx
import time
from pathlib import Path
import sys

GATEWAY_IP = "127.0.0.1"
PORT="31112"
FUNCTION_NAME = sys.argv[1]
URL = "http://{}:{}/function/{}".format(GATEWAY_IP, PORT, FUNCTION_NAME)

def convert_to_ms(num):
    return int(round(num*1000))

file_name = sys.argv[2]
payload = Path(file_name).read_text()
# payload = "my name is"

with httpx.Client() as client:
    start_time = time.monotonic()
    lent  = 0
    while lent < 1:
        r = client.post(URL, data=payload)
        lent = len(r.text)
        end_time = time.monotonic()
        response_time = convert_to_ms(end_time-start_time)
    print(r.text)
    print("*********")
    print('request_response_time: {}'.format(response_time))

