import requests
from bs4 import BeautifulSoup

def scrape_job_listings(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    job_listings = []
    
    for job in soup.find_all('div', class_='job_listing'):
        title = job.find('h2', class_='title').text.strip()
        company = job.find('div', class_='company').text.strip()
        location = job.find('div', class_='location').text.strip()
        # Extract more details as needed
        
        job_listings.append({
            'title': title,
            'company': company,
            'location': location,
            # Add more fields as needed
        })
    
    return job_listings

url = 'https://www.example-job-board.com/jobs'
job_listings = scrape_job_listings(url)
