from bs4 import BeautifulSoup
import requests
import csv
import json
import re
import pandas as pd
class CourseraScraper:
    ROOT = 'https://www.coursera.org'

    column_names = [
        'Name',
        'Url',
        'Rating',
        'Tags',
        'Description'
    ]

    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "referer": "//www.udemy.com/courses/search/?p=1&q=python",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
        }
    
    def __init__(self):
        with open('coursera.csv', 'w') as f:
            f.write(','.join(self.column_names) + '\n')

        
    def get_html(self, url): 
        return requests.get(url,headers=self.headers).text

    def parse_courses(self,html):
        result = []
        soup = BeautifulSoup(html, 'html.parser')
        mydivs = soup.find("body").find("script").text.split('{"context"')[1].split(',"plugins":{}};')[0][1::]
        json_object = json.loads(mydivs)
        courses = json_object['dispatcher']['stores']['AlgoliaResultsStateStore']['resultsState'][2]['content']['hits']
        for obj in courses:
            name = obj['name']
            url = self.ROOT + obj['objectUrl']
            tag = ', '.join(obj['skills']) 
            Rating = round(float(obj['avgProductRating']), 1)
            description = obj['_snippetResult']['description']['value']
            div = {'Name':name,'Url':url,'Rating':Rating,'Tags':tag ,'Description':description}
            result.append(div)
        
        return result

    def handle_scrap(self,fromPage,toPage):
        for i in range(fromPage, toPage):
            htmlContent = self.get_html(self.ROOT+f'/search?page={i}&index=prod_all_launched_products_term_optimization')
            try:
                Courses = self.parse_courses(htmlContent)
                self.save_csv(Courses)
            except:
                pass

    def save_csv(self,arr):
        df = pd.DataFrame(arr)
        df.to_csv('coursera.csv', mode='a',index=False, header=False)



if __name__ == '__main__':
    scraper = CourseraScraper()
    scraper.handle_scrap(1,84)
    print('__name__')
