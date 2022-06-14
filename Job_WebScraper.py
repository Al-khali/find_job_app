
import requests
from bs4 import BeautifulSoup
import pandas as pd

position = input("What position are you looking for? ")

location = input("What location do you want to search? ")

def extract(position, location_, page):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}

    url = f'https://fr.indeed.com/jobs?q={position}&l={location_}&start={page}'
    r = requests.get(url, headers)  
    soup = BeautifulSoup(r.content, 'html.parser') 
    return soup
def transform(soup):
    divs = soup.find_all('div', class_='job_seen_beacon')
    for item in divs:
        title = item.find('h2').text.strip('new')
          
        try: 
            location = item.find('div', class_='companyLocation').text.strip()
        except:
            location = ''
        company = item.find('span', class_='companyName').text.strip()
        try:
            salary = item.find('div', class_='attribute_snippet').text.strip()
        except:
            salary = ''      
        summary = item.find('div', class_='job-snippet').text.strip().replace('\n', '')
        job = {
            'title' : title,
            'location' : location,
            'company' : company,
            'salary' : salary,
            'summary' : summary
        }
        joblist.append(job)
    return



joblist = []
for i in range(0, 40, 10):
    print(f'Getting page, {i}')
    c = extract(position, location, 30)
    transform(c)


df = pd.DataFrame(joblist)
print(df.head())
df.to_csv('jobs.csv')