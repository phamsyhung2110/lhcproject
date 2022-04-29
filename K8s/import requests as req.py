# import requests as req
# for i in range(1000):
#     nginx = req.get("http://3.128.179.26:30704/")
#     print("request" + str(i))
#     if i == 1000:
#         print("done")
    
import requests
from concurrent.futures import ThreadPoolExecutor

def post_url(args):
    return requests.post(args[0], data=args[1])
    
form_data = {
    "foo1":"bar1",
    "foo2":"bar2"
}
list_of_urls = [("http://3.15.158.195/",form_data)]*100000


with ThreadPoolExecutor(max_workers=10) as pool:
    response_list = list(pool.map(post_url,list_of_urls))


for response in response_list:
    print(response)