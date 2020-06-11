from splinter import Browser
from yr import Yr
from accu import Accu
from pprint import pprint

WEATHERS = [Yr, Accu]

if __name__ == "__main__":
    results = {}
    with Browser(driver_name='chrome') as browser:
        for Weather in WEATHERS:
            weather = Weather()
            results[weather.name] = weather.download(browser)
    pprint(results)
