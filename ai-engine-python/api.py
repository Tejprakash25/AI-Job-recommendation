import json
import os
from fastapi import FastAPI
from matcher import calculate_match

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

resumes_path = os.path.join(BASE_DIR, "datasets", "resume.json")
jobs_path = os.path.join(BASE_DIR, "datasets", "jobs.json")

with open(resumes_path) as f:
    resumes = json.load(f)

with open(jobs_path) as f:
    jobs = json.load(f)

@app.get("/")
def home():
    return {"status": "AI Job Matcher Running"}

@app.get("/match")
def match_all():
    results = []

    for resume in resumes:
        for job in jobs:
            score = calculate_match(resume["text"], job["description"])
            results.append({
                "candidate": resume["name"],
                "job": job["title"],
                "score": score
            })

    return results
