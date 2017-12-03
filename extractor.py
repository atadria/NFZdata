from bs4 import BeautifulSoup
import urllib.request as url
import re


def extract_number_of_cardiograms_from(path):
    html = url.urlopen(path).read()
    soup = BeautifulSoup(html, "html.parser")
    return [elem.findNext('td').contents[0] for elem in soup.findAll("td", text=re.compile(".*[E,e]lektrokardiog*"))]


def get_sum_of_all_cardiograms_from(path):
    return sum(list(map(lambda e: int(e), extract_number_of_cardiograms_from(path))))
