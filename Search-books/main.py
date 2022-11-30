import part 
from part import has_page_dowld, has_text_title, has_text_link
from part import has_data_search

url="https://www.pagina12.com.ar"

def run(url):
    
    resul=has_page_dowld(url)
    
    resul = has_data_search(resul)
    
    agend = {
            
        }
        
    for i in resul:
        title = i.get_text()
        links = i.a.get('href')
        # print(title + ','  + links)
        
        
        # print(links,' ||| ', title)
         
        # 
        agend[title]=links
    # file = resul.find('div', attrs=('href'))
    
    # # print(resul)
    print(agend)

if "__main__" == __name__:
    run(url)
    

    
    # # print(result)
    
    # for job in result:
    #     try:
    #         titeElement = job.find("b", attrs={"class":'jsx-1327784995 copy2 primary jsx-2889528833 normal pod-subTitle subTitle-rebrand'}).get_text()
    #         # print(titeElement)
    #         company = job.find("b", attrs={"class" : "jsx-1327784995 title1 secondary jsx-2889528833 bold pod-title title-rebrand"}).get_text()
    #         # print(company)
    #         price = job.find("span", attrs={"class": "copy10 primary medium jsx-2889528833 normal line-height-22"})
    #         price = price.get_text()
    #         # print(price)
    #         brand = job.find("b", attrs={"class": "jsx-1327784995 copy2 primary jsx-2889528833 normal pod-sellerText seller-text-rebrand"}).get_text()
    #         # print(brand)
            
    #         link = job.find("a", attrs={"class": "jsx-3128226947"})['href']

    #         job = "Nombre: {}\nMarca: {}\nPrecio: {}\nTienda: {}\nLink: {}\n"
            
            
    #         job = job.format(titeElement, company, price, brand, link)
            
    #         print(job)
            
    #     except Exception as e:
    #         print("Exception {}".format(e))
            

