import requests

DURL = "https://www.roblox.com/download/https://www.roblox.com/download/client?os=mac"
request = requests.get(DURL)
Fname = request.url[DURL.rfind('/')+1:]
with open(Fname, 'wb') as f:
    for chunk in request.iter_content(chunk_size = 70000000000):
        if chunk:
            f.write(chunk)