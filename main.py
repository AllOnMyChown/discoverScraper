from bs4 import BeautifulSoup
from datetime import date
import requests
import calendar

# obtaining current month
today = date.today()
currentMonth = today.strftime("%B")

# setting array for months
monthList=[calendar.month_name[i] for i in range(1,12)]
monthIndex = monthList.index(currentMonth)

###################### logic for setting active trimester | needs to be changed if Discover categories ever last more than three months

# if current month is even set to previous month:
if (monthIndex % 2) == 0:
    currentMonth = monthList[monthIndex-1]

# scraping data from Discover calendar
headers = {
    "Connection": "keep-alive",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"
}

params = {
    "page": 20,
    "page_size": 25,
    "type": "image"
}
# request from live website
# html_text = requests.get('https://www.discover.com/credit-cards/cashback-bonus/cashback-calendar.html', headers=headers, params=params).text

# request from saved html file
with open('home.html', 'r') as html_text:
    content = html_text.read()

    scraper = BeautifulSoup(content, 'lxml')
# this may need to be changed if Discover updates website
    fiveCalendar = scraper.find_all('div', class_='col-xs-12 col-sm-6 col-lg-6 offer-mob-view')

    for category in fiveCalendar:
        categoryDate = category.h2.span.text.split()
        categoryText = category.h3.text

    # logic to find current active category
        if currentMonth in categoryDate:
            print(categoryText)
