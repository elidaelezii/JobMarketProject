import csv

def save_jobs(jobs, filename="jobs.csv"):
    if not jobs:
        return
    keys = jobs[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as f:
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(jobs)



