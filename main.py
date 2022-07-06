from bs4 import BeautifulSoup
import requests
import csv


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
        return requests.get(url)

    def parse_courses(self):
        return  {            
        'Name':'',
        'Url':'',
        'Rating':'',
        'Tags':'',
        'Description':''
        }

    def handle_scrap(self):
        return

    def save_csv(self):
        with open('coursera.csv', 'a') as f:
            writer = csv.DictWriter(f, self.column_names)
            writer.writerow()



if __name__ == '__main__':
    print('__name__')
