from read import reading, has_page_dowl,finding,has_data,finding_cult
import read
import os

def run():
  try:
    os.mkdir('noticias')
    links=reading()
    for i in range(len(links)-1):
      if i < len(links):
        page = has_page_dowl(links,i)
          
        soup = finding(page)
        
        if i == 3:
          soup=finding_cult(page)
        
        has_data(soup,page)
  except Exception as e:
    print("Error")
    print(e)
    print


if __name__ == "__main__":
     run()