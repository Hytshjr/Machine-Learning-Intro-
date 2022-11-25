import requests
from bs4 import BeautifulSoup

url="https://www.seek.com.au/python-jobs?salaryrange=100000-999999&salarytype=annual"
if "__main__" == __name__:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    
    def has_data_search(tag):
        return tag.has_attr("data-search-sol-meta")
    
    result = soup.find_all(has_data_search)
    
    # print(result)
    
    for job in result:
        try:
            titeElement = job.find("a", attrs={"data-automation": "jobTitle"}).get_text()
            print(titeElement,"/////////////////////")
            company = job.find("a", attrs={"data-automation" : "jobCompany"}).get_text()
            print(company)
            salary = job.find("span", attrs={"data-automation": "jobSalary"})
            salary = salary.get_text() if salary else 'n/a'
            print(salary)
 
            joblink= "https://www.seek.co.nz" + job.find("a", attrs={"data-automation": "jobTitle"})["href"]
            # print(joblink)
            
            job = "Titulo: {}\nEmpresa: {}\nSalario: {}\nLinks: {}a\n"
            
            job = job.format(titeElement, company, salary, joblink)
            
            # print(job)
            
        except Exception as e:
            print('"Exception {}".format(e)')
            