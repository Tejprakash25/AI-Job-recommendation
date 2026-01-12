import json
from pathlib import Path
from matcher import calculate_match

# Resolve paths relative to this script to avoid FileNotFoundError when
# running from a different working directory.
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "datasets"

# Load data
with open(DATA_DIR / "resume.json") as f:
    resumes = json.load(f)

with open(DATA_DIR / "jobs.json") as f:
    jobs = json.load(f)

print("\n=== AI Job Matching Results ===\n")

for resume in resumes:
    for job in jobs:
        # use .get() to be tolerant of missing keys
        score = calculate_match(resume.get("text", ""), job.get("description", ""))
        print(f"{resume.get('name', '<unknown>')} → {job.get('title', '<unknown>')} : {score}")
