from src.utils.constants import MINSA_URL
from src.utils.utils import get_soup_from_url, get_covid_links

url = MINSA_URL
soup = get_soup_from_url(url)
links = get_covid_links(soup)

for link in links:
    print(link)
