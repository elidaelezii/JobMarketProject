from collections import Counter

def top_skills(jobs):
    skills_list = [skill for job in jobs for skill in job.get("skills", [])]
    return dict(Counter(skills_list))

