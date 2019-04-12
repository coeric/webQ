#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

def BookList():

    url="https://www.books.com.tw/web/sys_hourstop/books?loc=act_menu_th_43_001"
    res=requests.get(url)
    soup=BeautifulSoup(res.content,'html.parser')
    data=soup.find('ul',attrs={'class':'clearfix'}).findAll('li',attrs={'class':'item'})
    for row in data:
        
        print row.strong.text,row.find('h4').text


if __name__=="__main__":
    BookList()