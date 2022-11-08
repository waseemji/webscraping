import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')

# print(soup.body.contents)
# print(soup.find_all('div'))
# print(soup.find(id='score_33504777'))
# print(soup.select('.score'))

links = soup.select('.titleline')
# votes = soup.select('.score')
subtext = soup.select('.subtext')
# print(votes) 
# points = ' guess this didnt work' 

def sort_stories_by_votes(hnlist):
    return sorted(hnlist,key= lambda k:k['votes'], reverse=True)


def create_custom_page(links,subtext):
    hn = []
    for idx,item in enumerate(links):
        title = item.getText()
        # print(title)
        href = item.find('a')
        url = href.get('href')

        # print(idx,href)
        vote = subtext[idx].select('.score')
        # print(points)
        if len(vote):
            points = int(vote[0].getText().replace('points',''))
            if points>100:
                hn.append({
                    'title':title,
                    'link':url,
                    'votes':points
                })
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_page(links,subtext))