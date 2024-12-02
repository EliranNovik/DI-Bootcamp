import requests
import time

def measure_load_time(url):
    try:
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()

        load_time = end_time - start_time
        return f"Time to load {url}: {load_time:.2f} seconds"
    except requests.exceptions.RequestException as e:
        return f"Failed to load {url}: {e}"

sites = ["https://www.google.com", "https://www.ynet.co.il", "https://www.imdb.com"]

for site in sites:
    print(measure_load_time(site))
