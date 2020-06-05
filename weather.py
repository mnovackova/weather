from splinter import Browser
import time


yr = {}

with Browser() as browser:
    # Visit URL
    url = "https://www.yr.no/place/Czech_Republic/Vysočina/Třebíč/hour_by_hour.html"
    browser.visit(url)

    table = browser.find_by_css('table.yr-table-hourly')[0]
    table1 = table.find_by_css('tbody')
    for number in range(17):
        row = table1.find_by_css('tr')[number] #prvni radek

        temperature = row.find_by_css('td')[2].text #teplota
        rain = row.find_by_css('td')[3].text #srazky v mm
        data = {"temperature": temperature, "rain": rain}

        time = row.find_by_css('td strong')[0].text #cas
        yr.update({time : data})


accu = {}

with Browser() as browser:
    # Visit URL
    url = "https://www.accuweather.com/cs/cz/třebíč/126627/hourly-weather-forecast/126627"
    browser.visit(url)

    time.sleep(15)
    number_of_date = len(browser.find_by_css('.date'))

    for number in range(number_of_date):
        time = browser.find_by_css('.date')[number].text.split()[0] #cas
        temperature = browser.find_by_css('.temp')[number].text #teplota
        rain = browser.find_by_css('.precip')[number].text.split()[-2] #srazky v %

        data =  {"temperature": temperature, "rain": rain}
        accu.update({time : data})

    import pdb; pdb.set_trace()

