from weather_base import WeatherBase

class Yr(WeatherBase):
    '''searching data in table'''
    url = "https://www.yr.no/place/Czech_Republic/Vysočina/Třebíč/hour_by_hour.html"
    name = "Yr"

    def download(self, browser):
        browser.visit(self.url)
        yr = {}

        table = browser.find_by_css('table.yr-table-hourly')[0]
        table_body = table.find_by_css('tbody')
        number_of_time = len(table_body.find_by_css('tr'))

        for number in range(number_of_time):
            row = table_body.find_by_css('tr')[number] #prvni radek

            temperature = row.find_by_css('td')[2].text #teplota
            rain = row.find_by_css('td')[3].text #srazky v mm
            data = {"temperature": temperature, "rain": rain}

            time = row.find_by_css('td strong')[0].text #cas
            yr.update({time : data})
        return yr