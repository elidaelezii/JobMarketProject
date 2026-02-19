import requests
from bs4 import BeautifulSoup

def scrape_jobs():
    url = "https://realpython.github.io/fake-jobs/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    jobs = []

    for card in soup.find_all("div", class_="card-content"):
        title = card.find("h2", class_="title").text.strip()
        company = card.find("h3", class_="company").text.strip()
        location = card.find("p", class_="location").text.strip()
        jobs.append({"title": title, "company": company, "location": location})
    return jobs
