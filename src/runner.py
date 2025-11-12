thonimport json
import requests
from extractors.infojobs_parser import parse_job_listings
from outputs.exporters import export_to_json
from config.settings import SETTINGS

def run_scraper():
    search_url = SETTINGS["search_url"]
    response = requests.get(search_url, headers=SETTINGS["headers"])
    
    if response.status_code == 200:
        job_listings = parse_job_listings(response.text)
        export_to_json(job_listings)
    else:
        print(f"Failed to fetch data: {response.status_code}")

if __name__ == "__main__":
    run_scraper()