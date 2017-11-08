#!usr/bin/env python

import requests
import pandas as pd
from bs4 import BeautifulSoup

addr = "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General"
resp = requests.get(addr)
html = resp.content
soup = BeautifulSoup(html,"html.parser")

tags = soup.find_all("tr","election_item")

lastyear = tags[0]
lastyear['id']

for t in tags:
    year = t.td.text
    year_id = t['id'][-5:]
    print(year, year_id,file=open('ElECTION_ID','a'))
