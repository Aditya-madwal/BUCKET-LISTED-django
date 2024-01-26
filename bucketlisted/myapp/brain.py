import requests
from bs4 import BeautifulSoup
import re


def get_data(urllink) :
    item_data={}
    specs_arr=[]
    specs_obj={}

    target_url=f"https://api.scrapingdog.com/scrape?api_key=65b27ba40ff088077baa70c7&url={urllink}"



    resp = requests.get(target_url)
    # print(resp.status_code)
    if(resp.status_code != 200):
        print(resp)
    soup=BeautifulSoup(resp.text,'html.parser')


    try:
        item_data["title"]=soup.find('h1',{'id':'title'}).text.lstrip().rstrip()
    except:
        item_data["title"]=None

    try:
        item_data["image"]=soup.find(id='landingImage')['src']
    except:
        item_data["image"]=None


    # images = re.findall('"hiRes":"(.+?)"', resp.text)
    # item_data["images"]=images

    try:
        # item_data["price"]=soup.find("span",{"class":"a-price-whole"})
        item_data['price'] = soup.find('span', {'class' : 'a-price-whole'}).string.replace(',','')
        item_data['price'] = int(item_data['price'])
    except:
        item_data["price"]=None

    specs = soup.find_all("tr",{"class":"a-spacing-small"})

    return(item_data)


print(get_data("https://www.amazon.in/gp/product/B0CPJG92ZS/ref=s9_bw_cg_Header_3b1_w?pf_rd_m=AT95IG9ONZD7S&pf_rd_s=merchandised-search-7&pf_rd_r=YM9FQJDGKCEE2ZTR30DK&pf_rd_t=101&pf_rd_p=4ebf4dd9-3c0a-4797-831e-0f00fc034435&pf_rd_i=1380263031"))