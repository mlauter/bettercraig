import requests
r = requests.get("url")
from bs4 import BeautifulSoup
ad = BeautifulSoup(r.text)
#to find description:
description = ad.find(id="postingbody").string #gives the stuff inside the tag
date_tag = soup.find(attrs={'class':'housing_movein_now property_date'}).string
