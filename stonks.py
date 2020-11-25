import requests
from bs4 import BeautifulSoup
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"}

class parser:
    def get(code):
        global headers
        if code == 'dollar':
            dollar = 'https://www.google.com/search?q=usd&oq=usd&aqs=chrome..69i57j0i131i433l2j0i433j0l4.3371j0j9&client=ubuntu&sourceid=chrome&ie=UTF-8'
            response = requests.get(dollar,headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            item = soup.findAll('span', {"class":'DFlfde', "class": 'SwHCTb', "data-precision": 2})
            return item[0].text
        elif code == 'eur':
            eur = 'https://www.google.com/search?client=ubuntu&hs=Iou&sxsrf=ALeKk03ugIQAH4eeiAkr4MGAdf9P5XdyBw%3A1606217789022&ei=PfC8X6xs6uGuBJGGucgH&q=eur&oq=eur&gs_lcp=CgZwc3ktYWIQAzIHCAAQsQMQQzIHCAAQsQMQQzIKCAAQsQMQgwEQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIECAAQQzIICAAQsQMQgwEyBAgAEEM6BAgAEEc6BwgjEOoCECc6CQgjECcQRhCCAjoECCMQJzoECC4QQzoNCC4QChABEEMQKhCTAjoJCAAQsQMQChABOgcILhCxAxBDOgUIABCxAzoCCAA6DQgAELEDEIMBEBQQhwJQpPO_AVjck8ABYKCYwAFoA3ACeAGAAYUCiAH6CZIBBTAuNS4ymAEAoAEBqgEHZ3dzLXdperABCsgBCMABAQ&sclient=psy-ab&ved=0ahUKEwjs_vvFi5vtAhXqsIsKHRFDDnkQ4dUDCA0&uact=5'
            response = requests.get(eur,headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            item = soup.findAll('span', {"class":'DFlfde', "class": 'SwHCTb', "data-precision": 2})
            return item[0].text
        elif code == 'grivn':
            grivn = 'https://www.google.com/search?client=ubuntu&sxsrf=ALeKk00YUfPXA-Gl5hF1BoggJnRv-4BQ0g%3A1606220940305&ei=jPy8X_6JEqaTwPAPi8qvuAI&q=griven&oq=griv&gs_lcp=CgZwc3ktYWIQAxgBMgIIADICCAAyBQguELEDMgIIADICCAAyAggAMgIILjIECAAQCjICCAAyBAgAEAo6BAgAEEc6BAgjECc6BwgAELEDEEM6DQgAELEDEIMBEBQQhwI6BAguEEM6BAgAEEM6BQgAELEDOggIABAKEAEQQzoHCCMQ6gIQJzoKCAAQsQMQgwEQQ1DAxwFYr-EBYKH4AWgBcAJ4AIABowGIAaMHkgEDMC42mAEAoAEBqgEHZ3dzLXdperABCsgBCMABAQ&sclient=psy-ab' 
            response = requests.get(grivn,headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            item = soup.findAll('span', {"class":'DFlfde', "class": 'SwHCTb', "data-precision": 2})
            return item[0].text
        elif code == 'tenge':
            tenge = 'https://www.google.com/search?client=ubuntu&sxsrf=ALeKk0071N1ykhHmrFySox3J9y0mFlfzHw%3A1606221004779&ei=zPy8X7aGL8j9rgTooqO4BQ&q=%D1%82%D0%B5%D0%BD%D0%B3%D0%B5+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D1%82%D0%B5%D0%BD%D0%B3%D0%B5+&gs_lcp=CgZwc3ktYWIQAxgAMgwIABCxAxBDEEYQggIyBAgAEEMyBAgAEEMyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAOgQIABBHOgQIIxAnOgcIABAUEIcCOgcIIxDqAhAnOgcILhAnEJMCOgUIABCxAzoICAAQsQMQgwE6BwgAELEDEEM6CAguELEDEJMCOgUILhCxAzoECAAQCjoCCC5QxCVYwE1gwlhoA3ACeASAAfsBiAHFE5IBBTAuNy42mAEAoAEBqgEHZ3dzLXdperABCsgBCMABAQ&sclient=psy-ab'
            response = requests.get(tenge,headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            item = soup.findAll('span', {"class":'DFlfde', "class": 'SwHCTb', "data-precision": 2})
            return item[0].text
        elif code == 'btc':    
            btc = 'https://www.google.com/search?client=ubuntu&hs=Kgv&sxsrf=ALeKk01Itwohgnwei-gNQ0Bq1rKsA0RarQ%3A1606221139536&ei=U_28X6yeIN6GwPAPu52VUA&q=%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD&oq=%D0%B1%D0%B8%D1%82%D0%BA%D0%BE%D0%B8%D0%BD&gs_lcp=CgZwc3ktYWIQAzIMCAAQFBCHAhBGEIICMggIABCxAxCDATIICAAQsQMQgwEyDQgAELEDEIMBEBQQhwIyCAgAELEDEIMBMgUIABCxAzIFCAAQsQMyAggAMggIABCxAxCDATIICAAQsQMQgwE6BAgAEEc6BAgjECc6BwgjEOoCECc6AgguOggILhCxAxCDAToFCC4QsQM6BAgAEEM6BwgAELEDEEM6BwgAEBQQhwJQgIAEWOedBGCMogRoAXACeASAAaEBiAGoDZIBBDAuMTKYAQCgAQGqAQdnd3Mtd2l6sAEKyAEIwAEB&sclient=psy-ab&ved=0ahUKEwjsk8-DmJvtAhVeAxAIHbtOBQoQ4dUDCA0&uact=5'
            response = requests.get(btc,headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            item = soup.findAll('span', {"class":'DFlfde', "class": 'SwHCTb', "data-precision": 2})
            return item[0].text
        elif code == 'eth': 
            ethereum = 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+ethereum&oq=%D0%BA%D1%83%D1%80%D1%81+ethereum&aqs=chrome.0.0i131i433j0l4.5087j0j9&client=ms-android-xiaomi&sourceid=chrome-mobile&ie=UTF-8'
            response = requests.get(ethereum,headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            item = soup.findAll('span', {"class":'DFlfde', "class": 'SwHCTb', "data-precision": 2})
            return item[0].text
#covid_19 = 'hhttps://www.worldometers.info/coronavirus/#countries'
#response = requests.get(covid_19,headers=headers)

#soup = BeautifulSoup(response.content, 'html.parser')
#item = soup.findAll('span', {"class":'DFlfde', "class": 'SwHCTb', "data-precision": 2})
#item = soup.findAll('h2', {"class":'info_blk stat_block confirmed'
#a = parser.get('eth')
#print(a)

