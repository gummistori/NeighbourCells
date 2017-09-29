from bs4 import BeautifulSoup
import os
import re

filename_input = 'SSiteAcc.html'
filename_output = 'accList.csv'

with open(filename_input, 'r') as file:
    data = file.read()
file.close()

soup = BeautifulSoup(data, 'html.parser')
so = soup.getText()

lis = []
for s in soup('tr'):
    line = s.get_text().split('\n')
    if len(line[4]) > 0 and line[2] != 'Site Alias':
        it = (line[2], line[4])
        lis.append(it)


with open(filename_output, 'w') as file:
	#file.write('Site1,Site2\n')
	for i in lis:
		file.write(i[0]+','+i[1]+'\n')

