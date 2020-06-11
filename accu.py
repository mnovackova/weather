from weather_base import WeatherBase

class Accu(WeatherBase):
    '''searching data in page'''

    url = "https://www.accuweather.com/cs/cz/třebíč/126627/hourly-weather-forecast/126627"
    name = "Accu"

    def download(self, browser):
        browser.visit(self.url)
        accu = {}

        cards = browser.find_by_css('.hourly-forecast-card', wait_time=5)


        for row in cards:
            time = row.find_by_css('.date').text #cas

            while not time: # kontroluje jestli je cas obsaze a pripadne scroluje
                row.scroll_to()
                time = row.find_by_css('.date').text #cas

            time_update = time.split()[0]
            temperature = row.find_by_css('.temp').text #teplota
            rain = row.find_by_css('.precip').text.split()[-2] #srazky v %

            data =  {"temperature": temperature, "rain": rain}
            accu.update({time_update : data})
        return accu





