thonfrom bs4 import BeautifulSoup

def parse_job_listings(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    job_listings = []
    
    for job in soup.find_all('div', class_='job-offer'):
        title = job.find('a', class_='job-title').text.strip()
        description = job.find('p', class_='job-description').text.strip()
        company = job.find('span', class_='company-name').text.strip()
        location = job.find('span', class_='location').text.strip()
        contract_type = job.find('span', class_='contract-type').text.strip()
        published_at = job.find('time', class_='published-at').text.strip()
        link = job.find('a', class_='job-title')['href']

        job_listings.append({
            "title": title,
            "description": description,
            "company": company,
            "location": location,
            "contractType": contract_type,
            "publishedAt": published_at,
            "link": link
        })
    
    return job_listings