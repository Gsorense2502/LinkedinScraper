#!/usr/bin/env python

from bs4 import BeautifulSoup, Comment
import json

html_file = open('./sample_html/sample1.html', 'r', encoding='UTF-8')

soup = BeautifulSoup(html_file, 'html.parser')

data = soup.find('code', {'id': 'streamed-content-content'})

comments = data.find(string=lambda text: isinstance(text, Comment))

soup_string = str(comments)
x = json.loads(soup_string)
results = x['searchResults']

for result in results:
    print(result['name'], result['location'], result['size'])

print(len(results))
