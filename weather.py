from splinter import Browser

'''
yr = {}

with Browser() as browser:
    # Visit URL
    url = "https://www.yr.no/place/Czech_Republic/Vysočina/Třebíč/hour_by_hour.html"
    browser.visit(url)

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
'''

accu = {}

with Browser(driver_name='chrome') as browser:
    # Visit URL
    url = "https://www.accuweather.com/cs/cz/třebíč/126627/hourly-weather-forecast/126627"
    browser.visit(url)


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

#import pdb; pdb.set_trace()




