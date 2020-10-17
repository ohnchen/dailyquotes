#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
import re

url = "https://www.brainyquote.com/quote_of_the_day" 
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

quote = re.findall(r"title=\"view quote\">(.*?)<", str(soup))
author = re.findall(r"title=\"view author\">(.*?)<", str(soup))

print(quote[1], author[0])
