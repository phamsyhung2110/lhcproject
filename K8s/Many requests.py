import requests
from concurrent.futures import ThreadPoolExecutor

def get_url(url):
    return requests.get(url)

list_of_urls = ["http://3.17.190.2/"]*100000

with ThreadPoolExecutor(max_workers=10) as pool:
    response_list = list(pool.map(get_url,list_of_urls))

for response in response_list:
    print(response)