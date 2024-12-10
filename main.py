import requests as rq
from bs4 import BeautifulSoup  as bs

def get_all_links(url,domain_url):
    response = rq.get(url)

    if response.status_code != 200:
        print("Error fetching the page.")
        return []

    soup = bs(response.text, 'html.parser')

    links_on_page = []
    for a_tag in soup.find_all('a', href=True):
        links_on_page.append(a_tag['href'])
    output_list = [s for s in links_on_page if s.startswith(domain_url)]
    unique_list = list(set(output_list))
    return unique_list


def get_all_urls(domain_url):
    links = get_all_links(domain_url)
    for url in links:
        links = links + get_all_links(url,domain_url)
        links = list(set(links))
    return links
list_all_urls = get_all_urls(domain_url)
print(list_all_urls)
