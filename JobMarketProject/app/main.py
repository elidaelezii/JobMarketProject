from scraper.scraper import scrape_jobs
from api_clients.enrichment import enrich_jobs
from processing.analytics import top_skills
from security.encryption import encrypt_value
from storage.database import save_jobs

def run():
    jobs = scrape_jobs()
    jobs = enrich_jobs(jobs)
    
    print("Top Skills:", top_skills(jobs))
    
    for job in jobs:
        job["title"] = encrypt_value(job["title"])
    
    save_jobs(jobs)
    print("Encrypted Job Titles:")
    for job in jobs:
        print(job["title"])

if __name__ == "__main__":
    run()
