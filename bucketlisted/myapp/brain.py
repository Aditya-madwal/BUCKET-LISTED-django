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
        item_data['price'] = soup.find('span', {'class' : 'a-price-whole'}).string.replace(',','.')
        item_data['price'] = int(item_data['price'])
    except:
        item_data["price"]=None

    try:
        item_data["rating"]=soup.find("i",{"class":"a-icon-star"}).text
    except:
        item_data["rating"]=None


    specs = soup.find_all("tr",{"class":"a-spacing-small"})

    for u in range(0,len(specs)):
        spanTags = specs[u].find_all("span")
        specs_obj[spanTags[0].text]=spanTags[1].text

    return(item_data)


# get_data('https://www.amazon.in/YONEX-Easy22-Badminton-Shorts-India/dp/B0BTSBPPFV/ref=sl_ob_desktop_dp_0_1_v2?_encoding=UTF8&pd_rd_w=xqhs6&content-id=amzn1.sym.4f357184-dbe5-49df-beb3-916493375ee4&pf_rd_p=4f357184-dbe5-49df-beb3-916493375ee4&pf_rd_r=9EKAJ6Z2PYRT5YB698S6&pd_rd_wg=QIyZg&pd_rd_r=628ab21d-e292-46f0-bca1-17991111f9cb')