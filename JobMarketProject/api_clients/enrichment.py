# api_clients/enrichment.py
def enrich_jobs(jobs):
    for job in jobs:
        job["skills"] = ["Python", "SQL","Hacking","Cyber Security","AI"]  # shembull i thjeshtë
    return jobs

