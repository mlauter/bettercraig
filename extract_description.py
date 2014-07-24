import requests, os
from bs4 import BeautifulSoup

#enter search query
search_page = requests.get("http://newyork.craigslist.org/search/sub?maxAsk=1500&query=august")

#get all links for search results, filter irrelevant ones
search_res = BeautifulSoup(search_page.text)
links = {l for l in [link.get('href') for link in search_res.find_all('a')] if l.endswith('.html')}

#filter out irrelevant links, make a full url, follow the link, get the info
with open("ads.txt", 'w') as f:
    for link in links:
        try:
            ad = BeautifulSoup(requests.get("http://newyork.craigslist.org"+link).text)
            description = ad.find(id='postingbody').string.strip()
            date_tag = ad.find(attrs={'class':'housing_movein_now property_date'}).string
            print description, date_tag
        except:
            print link
            print ad.getText
        f.write('\n'+'\t'.join([date_tag, description])+'\n')
#to find description:
#description = ad.find(id="postingbody").string #gives the stuff inside the tag
#date_tag = soup.find(attrs={'class':'housing_movein_now property_date'}).string