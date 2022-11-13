from src.utils.constants import MINSA_URL, MINSA_PAGINATOR_TAG, MINSA_PAGINATOR_CLASS, MINSA_PAGE_CLASS
from src.utils.utils import get_soup_from_url, get_covid_links, get_paging

soup = get_soup_from_url(MINSA_URL)
links = get_covid_links(soup)
# last_page = get_paging(soup, MINSA_PAGINATOR_TAG, MINSA_PAGINATOR_CLASS, MINSA_PAGE_CLASS)

for link in links:
    print(link)

# print(last_page)
