# Write a function that will call a given HTTP endpoint exactly 5 times a second.
# Assume that the HTTP endpoints average response time is 450ms

# https://code.activestate.com/recipes/413137-call-a-functionmethod-x-times-per-second/#c3
import time
from concurrent.futures.thread import ThreadPoolExecutor
from urllib.request import urlopen


def poll_url(url: str, requests_per_sec: int = 5, limit: int = 3):
    start = time.time()
    n = 0
    while n <= limit if limit else True:
        with ThreadPoolExecutor(max_workers = 3) as executor:
            for _ in range(requests_per_sec):
                future = executor.submit(urlopen, url)
                print(future.result())
        while time.time() - start < 1:
            time.sleep(0.01)
        print(time.time() - start)
        start = time.time()
        n += 1


if __name__ == "__main__":
    poll_url('https://index.hu')
