import requests
from bs4 import BeautifulSoup as bs4

headers = {
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

url = "https://cars.av.by/audi"
session = requests.Session()
# file = open('cars.txt', 'w+')
try:
    req = session.get(url, headers=headers)
    if req.status_code == 200:
        soup = bs4(req.content, 'html.parser')
        divs = soup.find_all('div', attrs={'class': 'listing-item listing-item--color listing-item--top'})
        # print(divs)
        # soup_cost = bs4(req.content, 'html.parser')
        # cost = soup_cost.find('div', attrs={'class': 'listing-item__priceusd'})
        # costs = soup.find_all('div', attrs={'class': 'listing-item__priceusd'})
        # for cost in costs:
        #     price = cost.text
        #     print(price)

        for div in divs:
            title = div.find('a').text
            href = div.find('a')['href']
            price = str(div.find('div', attrs={'class': 'listing-item__priceusd'}).text)
            # cost = ''
            # for p in price:
            #     if p >= '0' and p <= '9':
            #         cost += p
            # cost = int(cost)
            # print(cost)
            # if cost <= 15000:
            #     print("{} - https://cars.av.by{} {}".format(title, href, cost))
            # file.write("{} - https://cars.av.by{}".format(str(title), str(href)) + "\n")
            print("{} - https://cars.av.by{} {}".format(title, href, price))
    else:
        print("Error!")
except Exception:
    print("Error in url!")
# file.close()

