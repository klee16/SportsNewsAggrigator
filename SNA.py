import webbrowser
import html

from feedsearch import search

import sys

stdoutOrigin=sys.stdout
sys.stdout = open("log.txt", "w")

feeds = search('https://apnews.com/sports')


urls = [f.url for f in feeds]

print(urls)

import feedparser
import time
if len(urls) > 0:
  news_feed = feedparser.parse(urls[0])
  entries = news_feed["entries"]
  count=0
  for entry in entries:
    count = count + 1
    print(
     str(count) + ". " + entry["title"] \
     + "\n\t\t" + entry["published"] \
     + "\n\t\t" + entry["link"]\
     + "\n\n"
     )
    time.sleep(0.33)


#FEED2
feeds2 = search('https://www.foxsports.com/')


urls = [f.url for f in feeds2]
print(urls)
if len(urls) > 0:
  news_feed = feedparser.parse(urls[0])
  entries = news_feed["entries"]
  count=0
  for entry in entries:
    count = count + 1
    print(
     str(count) + ". " + entry["title"] \
     + "\n\t\t" + entry["published"] \
     + "\n\t\t" + entry["link"]\
     + "\n\n"
     )
    time.sleep(0.33)


#FEED3
feeds3 = search('https://theathletic.com/')


urls = [f.url for f in feeds3]
print(urls)
if len(urls) > 0:
  news_feed = feedparser.parse(urls[0])
  entries = news_feed["entries"]
  count=0
  for entry in entries:
    count = count + 1
    print(
     str(count) + ". " + entry["title"] \
     + "\n\t\t" + entry["published"] \
     + "\n\t\t" + entry["link"]\
     + "\n\n"
     )
    time.sleep(0.33)

sys.stdout.close()
sys.stdout=stdoutOrigin

with open('log.txt', 'r') as file:
    text = file.read()

    html_text = '<html>\n<body><h1> Sports News Feed </h1>\n'
    html_text += '<html>\n<body><h2> Fox Sports. AP News . The Athletic </h2>\n'



    for line in text.split('\n'):
        html_text += f'<p>{line}</p>\n'

    html_text += '</body>\n</html>'


    with open('log.html', 'w') as file:
        file.write(html_text)



webbrowser.open_new_tab('log.html')