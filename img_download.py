import random
import requests

get = str(input("Enter url of image to Download : "))

def download_img(url):
    print("downloding...")
    name = random.randrange(1, 1000)
    full_name = str(name)+".jpg"
    r = requests.get(url, stream=True)
    with open(full_name,'wb') as f:
        f.write(r.content)
    return "download completed. saved as name :" + full_name

print(download_img(get))    
