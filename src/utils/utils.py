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


def get_paging(soup, paginator_tab, paginator_class, page_class):
    paging = soup.find_all(paginator_tab, {'class': paginator_class})
    print(paging)
    paging_link = paging[0].find_all('span', {'class': page_class})
    print(paging_link)
    last_page = int([item.get('href').split('/')[-1] for item in paging_link][-1])

    return last_page


def paging_loop(soup, paginator_tag):
    return 0


