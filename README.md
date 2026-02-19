# JobMarketProject

Ky projekt është një pipeline modulare për nxjerrjen, përpunimin, analizën, enkriptimin dhe ruajtjen e të dhënave të punëve (job listings).
Struktura është e ndarë në module, secili me funksion specifik:

scraper → nxjerr të dhëna live nga një faqe demo: title, company, location.

api_clients → pasuron të dhënat me aftësi (skills) ose fusha shtesë.

processing → analizon aftësitë më të kërkuara për të identifikuar trendet.

security → enkripton titujt e punës për ruajtje të sigurt.

storage → ruan të dhënat e përpunuara për përdorim të mëvonshëm.

app/main.py → entry point që ekzekuton të gjithë pipeline-in nga fillimi deri te output.


Strukturimi i Folderave
JobMarketProject/
│
├─ app/
│   ├─ main.py        # Entry point i projektit
│   └─ __init__.py
│
├─ scraper/
│   ├─ scraper.py      # Funksioni scrape_jobs() nxjerr tituj, kompani dhe vendndodhje
│   └─ __init__.py
│
├─ api_clients/
│   ├─ enrichment.py   # Logjika për pasurimin e të dhënave
│   └─ __init__.py
│
├─ processing/
│   ├─ analytics.py    # Funksione për analizën e aftësive më të kërkuara
│   └─ __init__.py
│
├─ security/
│   ├─ encryption.py   # Enkriptimi i titujve të punëve
│   └─ __init__.py
│
├─ storage/
│   ├─ database.py     # Ruajtja e të dhënave (p.sh. në file ose database)
│   └─ __init__.py


Rrjedha e të Dhënave:

* Scraping
scraper.scraper.scrape_jobs() merr të dhëna live nga:
Fake Jobs Demo
Nxjerr për secilin job: title, company, location.

*Enrichment
api_clients.enrichment.enrich_jobs() mund të përdoret për të shtuar fushat ekstra, si skills ose job level.
Processing / Analytics
processing.analytics.top_skills() analizon të dhënat dhe nxjerr aftësitë më të kërkuara nga titujt ose description.

*Security / Encryption
security.encryption.encrypt_value() enkripton titujt e punës (p.sh. për ruajtje të sigurt ose për demonstrim të pipeline-it).

*Storage
storage.database.save_jobs() ruan të dhënat e përpunuara për përdorim të mëtejshëm ose analizë.

*Main.py
app.main.run() ekzekuton të gjithë pipeline-in:
Scrape → Enrich → Analytics → Encrypt → Save → Output

*Libraritë dhe Teknologjitë e Përdorura
Python 3.12
requests – për kërkesat HTTP dhe scraping
BeautifulSoup – për parsimin e HTML
collections.Counter – për analizën e aftësive më të kërkuara
Funksione modulare dhe strukturë me __init__.py

*Enkriptimi
Titujt e punëve enkriptohen me një funksion të thjeshtë të demonstruar (encrypt_value)
Mund të zëvendësohet me enkriptim real (Fernet/AES) për siguri reale.

Udhëzime për Ekzekutim:
Sigurohu që Python 3 është instaluar.
Instaloni libraritë e nevojshme:
pip install requests beautifulsoup4
collections.Counter – për analizën e aftësive më të kërkuara
Funksione modulare dhe strukturë me __init__.py
Shko në folderin kryesor të projektit dhe ekzekuto:

python -m app.main


Do të shfaqen:
Titujt e enkriptuar të punës
Top skills nga analiza

Output Shembull
Top Skills: {'Python': 100, 'SQL': 100, 'Cyber Security': 100, 'AI': 100}
Encrypted Job Titles:
repoleveD nohtyP roineS
reenigne ygrenE
evitucexe lageL

│
└─ jobs.html           # Fshihet, nuk përdoret më (përdorim live scraping)
