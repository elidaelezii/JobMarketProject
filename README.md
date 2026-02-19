JobMarketProject

This project is a modular pipeline for extracting, processing, analyzing, encrypting, and storing job listing data. The architecture is divided into modules, each with a specific responsibility:

scraper → Extracts live data from a demo job site: title, company, location.

api_clients → Enriches the data with additional fields such as skills or job level.

processing → Analyzes the most requested skills to identify trends.

security → Encrypts job titles for secure storage.

storage → Saves the processed data for later use.

app/main.py → Entry point that executes the entire pipeline from start to finish.

Folder Structure
JobMarketProject/
├─ app/
│   ├─ main.py        # Project entry point
│   └─ __init__.py

├─ scraper/
│   ├─ scraper.py     # scrape_jobs() function extracts title, company, location
│   └─ __init__.py

├─ api_clients/
│   ├─ enrichment.py  # Logic to enrich job data
│   └─ __init__.py

├─ processing/
│   ├─ analytics.py   # Functions for skill analysis
│   └─ __init__.py

├─ security/
│   ├─ encryption.py  # Job title encryption
│   └─ __init__.py

├─ storage/
│   ├─ database.py    # Saving processed job data
│   └─ __init__.py

Data Flow:

*Scraping
scraper.scraper.scrape_jobs() fetches live job data from the Fake Jobs Demo site
 and extracts: title, company, location.

*Enrichment
api_clients.enrichment.enrich_jobs() can add extra fields like skills or job level.

*Processing / Analytics
processing.analytics.top_skills() analyzes job data to determine the most requested skills from titles or descriptions.

*Security / Encryption
security.encryption.encrypt_value() encrypts job titles for secure storage or demonstration purposes.

*Storage
storage.database.save_jobs() saves the processed data for later use or analysis.

*Pipeline Execution
app.main.run() executes the full pipeline:

Scrape → Enrich → Analytics → Encrypt → Save → Output

Libraries and Technologies Used:

Python 3.12
requests – for HTTP requests and scraping
BeautifulSoup – for parsing HTML
collections.Counter – for analyzing top skills
Modular Python structure using __init__.py files

Encryption:
Job titles are encrypted using a simple demonstration function (encrypt_value).
For real security, this can be replaced with Fernet/AES encryption.

How to Run:

Make sure Python 3 is installed.
Install required libraries:

pip install requests beautifulsoup4

Navigate to the main project folder and run:

python -m app.main

The script outputs:

Encrypted job titles

Top skills from the analysis

Example Output:
Top Skills: {'Python': 100, 'SQL': 100, 'Cyber Security': 100, 'AI': 100}
Encrypted Job Titles:
Senior Python Developer
Energy Engineer
Legal Executive
...
