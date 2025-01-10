import requests
import time

TARGET_URL = "http://1.2.3.69/"
TIME_INTERVAL = 0.1
COUNT = 0
running = True


while running:
    try:
        print("Sending the fucking request...")
        response = requests.get(TARGET_URL)
        COUNT+=1
        print(f"Response with status code:{response.status_code}, request count: {COUNT}")
        time.sleep(TIME_INTERVAL)
    except requests.exceptions.RequestException as e:
        print(f"Getting this fucking Error: {e}")
        break
    except KeyboardInterrupt:
        break