from bs4 import BeautifulSoup as bs
import requests as rq


def get_soup_from_url(url):
    html = rq.get(url).content.decode('utf-8')
    soup = bs(html, 'html.parser')
    return soup


def get_covid_links(soup):
    covid_links = []
    covid_references = soup.select("a[href*='covid']")
    for reference in covid_references:
        covid_links.append(reference['href'])

    return covid_links


