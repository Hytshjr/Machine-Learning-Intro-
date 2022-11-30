import openpyxl
import os
import requests
from bs4 import BeautifulSoup

def reading():
    archivo = "/mnt/d/Github/Search-books/web_scrapping/links.xlsx"
    book = openpyxl.load_workbook(archivo, data_only=True)
    hoja = book.active
    
    
    celdas = hoja['B2':'B8']
    lista =[]
    
    for fila in celdas:
        for celdas in fila:
            lista.append(celdas.value)
    return lista
    


def has_page_dowl(links,i):
    try:
        page = requests.get(links[i])
        soup = BeautifulSoup(page.text, 'lxml')
        return soup
    except Exception as e:
        print("Error en el link" + page)
        print(e)


def finding(page):
    return page.find_all('div', attrs={'class' : 'article-item__content'})



def finding_cult(page):
    return page.find_all('div', attrs={'class' : 'article-box__container'})



def has_data(soup,page):
    name_file= page.find('title').get_text()
    file = open('noticias/'+name_file+".txt", "w")
    for i in soup:
        
        links = i.a.get('href')
        title = i.find('a').get_text()
        file.write(title+": -"+'    https://www.pagina12.com.ar'+links+ '\n')
        
    print(name_file)
