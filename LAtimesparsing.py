# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 07:24:51 2021

@author: slim_
"""

import csv
import re
import requests
page = requests.get("http://maps.latimes.com/neighborhoods/neighborhood/list/")

from bs4 import BeautifulSoup

soup = BeautifulSoup(page.content, 'html.parser')

sub1 = '/neighborhoods/neighborhood/'
sub2 = '/neighborhoods/region/'

neighborhoods = ['City']
regions = ['Region']

for td in soup.find_all('td'):
    for a in td.find_all('a', href=re.compile(sub1)):
        for e in a.contents:
            neighborhoods.append(e)
    for a2 in td.find_all('a', href=re.compile(sub2)):
        for e2 in a2.contents:
            regions.append(e2)            


with open('C:/Users/slim_/OneDrive/Documents/LA.csv', 'w', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(zip(neighborhoods, regions))
    
#with open('C:/Users/slim_/OneDrive/Documents/LA.csv', 'r') as in_file:
#    with open('C:/Users/slim_/OneDrive/Documents/LA_no_empty_rows.csv', 'w') as out_file:
#        writer_empty = csv.writer(out_file)
#        for row in csv.reader(in_file):
#            if any(row):
#                writer_empty.writerow(row)
