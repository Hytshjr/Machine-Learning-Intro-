import requests
from bs4 import BeautifulSoup

url="https://www.falabella.com.pe/falabella-pe/brand/SAMSUNG"

if "__main__" == __name__:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    
    def has_data_search(tag):
        return tag.has_attr("pod-layout")
    
    result = soup.find_all(has_data_search)
    
    # print(result)
    
    for job in result:
        try:
            titeElement = job.find("b", attrs={"class":'jsx-1327784995 copy2 primary jsx-2889528833 normal pod-subTitle subTitle-rebrand'}).get_text()
            # print(titeElement)
            company = job.find("b", attrs={"class" : "jsx-1327784995 title1 secondary jsx-2889528833 bold pod-title title-rebrand"}).get_text()
            # print(company)
            price = job.find("span", attrs={"class": "copy10 primary medium jsx-2889528833 normal line-height-22"})
            price = price.get_text()
            # print(price)
            brand = job.find("b", attrs={"class": "jsx-1327784995 copy2 primary jsx-2889528833 normal pod-sellerText seller-text-rebrand"}).get_text()
            # print(brand)
            
            link = job.find("a", attrs={"class": "jsx-3128226947"})['href']

            job = "Nombre: {}\nMarca: {}\nPrecio: {}\nTienda: {}\nLink: {}\n"
            
            
            job = job.format(titeElement, company, price, brand, link)
            
            print(job)
            
        except Exception as e:
            print("Exception {}".format(e))
            

