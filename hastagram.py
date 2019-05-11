import os
from requests import get
from bs4 import BeautifulSoup

def clear():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')

clear()
asci = """  

 _    _           _                                  
| |  | |         | |                                 
| |__| | __ _ ___| |_ __ _  __ _ _ __ __ _ _ __ ___  
|  __  |/ _` / __| __/ _` |/ _` | '__/ _` | '_ ` _ \ 
| |  | | (_| \__ \ || (_| | (_| | | | (_| | | | | | |
|_|  |_|\__,_|___/\__\__,_|\__, |_|  \__,_|_| |_| |_|
                            __/ |                    
                           |___/                     

=======================================
Coded By Nor Ahmad
Github : https://github.com/archive-code
Website : http://hepiweb.fun
Instagram : http://instagram.com/norahm4d 
Note : Hastagram untuk mengecek hastag terpopuler
=======================================
"""
print (asci)
hastag = input('Masukkan Hastag : ')
url = get("https://web.stagram.com/search?query=" + hastag)

soup = BeautifulSoup(url.text, 'html.parser')
tags = soup.findAll('div',{'class':'card min-height'})
for tag in tags:
  a =  tag.find('a').get('href')
  if 'tag' in a.lower():
    print('a)
    data = tag.find('div',{'class':'card-block text-center'}).text
    print (data)
