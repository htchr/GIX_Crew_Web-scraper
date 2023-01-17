import requests
from bs4 import BeautifulSoup

sites = ["https://gixlabs.github.io"]
sites_dict = {"https://gixlabs.github.io": None}

for s in sites:
    try:
        r = requests.get(s)
        code = int(r.status_code)
        # print(code, " - ", s)
        sites_dict[s] = code
        if code < 400:
            data = r.text
            soup = BeautifulSoup(data, features="html.parser")
            links = [link.get("href") for link in soup.find_all("a", href=True) if "https" not in link.get("href")]
            for l in links:
                link_site = sites[0] + l
                if link_site not in sites_dict:
                    sites_dict[link_site] = None
                    sites.append(link_site)
    except:
        sites_dict[s] = "Error"

for s in sites_dict.keys():
    if sites_dict[s] == "Error" or sites_dict[s] >= 400:
        print(sites_dict[s], " - ", s)
