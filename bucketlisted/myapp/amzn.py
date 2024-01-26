import requests

def get_ASIN(pro_url) :
    pro_url = pro_url.split('/')
    for i in pro_url :
        if len(i) == 10 :
            return i


def get_product_data(urllink) :
    url = "https://api.scrapingdog.com/amazon/product"
    params = {
        "api_key": "65b27ba40ff088077baa70c7",
        "domain": "in",
        "asin": get_ASIN(pro_url=urllink)
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        # print(data)
        item_name = data['title']
        item_price = int(data['price'].replace(',','')[1:])
        item_image_src = data['images'][0]

        return {'name':item_name,'price':item_price,'img_src':item_image_src}

    else:
        # print(f"Request failed with status code {response.status_code}")
        return
    return



