import requests
from bs4 import BeautifulSoup
#scrapping pmids of the pdfs from NIH without page number parameter
def scrap_Pmid_WOPage(url):
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        #docsum-pmid pmid class name
        pmid = soup.find_all('span', class_='docsum-pmid')

        for pmidN in pmid:
            print("Pmids from page1",pmidN.text)
    else:
        print('Failed. Status code:', response.status_code)
url_WO_Page = "https://pubmed.ncbi.nlm.nih.gov/?term=%28%221995%22%5BDate+-+Publication%5D+%3A+%223000%22%5BDate+-+Publication%5D%29+genes"
scrap_Pmid_WOPage(url_WO_Page)

#scrapping pmids of the pdfs from NIH with page number parameter
def scrap_Pmid_WPage(url,i):
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        #docsum-pmid pmid class name
        pmid = soup.find_all('span', class_='docsum-pmid')

        for pmidN in pmid:
            print("pmids from page"+str(i),pmidN.text)
    else:
        print('Failed. Status code:', response.status_code)
for i in range(5):
    
    url_WPage = "https://pubmed.ncbi.nlm.nih.gov/?term=(%221995%22%5BDate%20-%20Publication%5D%20%3A%20%223000%22%5BDate%20-%20Publication%5D)%20genes&page="+str(i)
    scrap_Pmid_WPage(url_WPage,i)