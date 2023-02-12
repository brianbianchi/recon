import requests
import sys

# Test status of disallowed robots.txt routes

base = sys.argv[1] # "https://www.blackbaud.com/"

r = requests.get(base + "robots.txt")
lines = r.text.splitlines()

for line in lines:
    if line.startswith("Disallow: /"):
        route = line.split("Disallow: /", 1)[1]
        rr = requests.get(base + route)
        print(rr.status_code, rr.url)
