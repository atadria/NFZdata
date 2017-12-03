from selenium import webdriver
from selenium.webdriver.support.ui import Select

path = 'https://prog.nfz.gov.pl/app-jgp/KatalogJGP.aspx'

driver = webdriver.Firefox()
driver.get(path)

options = []
options_text_dict = {}
select = Select(driver.find_element_by_name('ctl00$ContentPlaceHolder2$ddlSymylacjaJGP'))
for option in select.options:
    options.append(option.get_attribute('value'))
    options_text_dict[option.get_attribute('value')] = option.text

options = options[1:]

all_links_from_year = {}

# select years
for option in options:
    select = Select(driver.find_element_by_name('ctl00$ContentPlaceHolder2$ddlSymylacjaJGP'))
    select.select_by_value(option)
    options2 = []
    all_links_from_year[options_text_dict[option]] = []
    select2 = Select(driver.find_element_by_name('ctl00$ContentPlaceHolder2$ddlKatalogJGP'))
    # select disease
    for option2 in select2.options:
        options2.append(option2.get_attribute('value'))

    links_from_year = []

    for option2 in options2:
        select3 = Select(driver.find_element_by_name('ctl00$ContentPlaceHolder2$ddlKatalogJGP'))
        select3.select_by_value(option2)
        elinks = []
        elinks = driver.find_elements_by_xpath("//a[@href]")
        links = []
        for elink in elinks:
            links.append(elink.get_attribute('href'))
        links_from_year += links[3:]
    all_links_from_year[options_text_dict[option]] = links_from_year

with open('links.txt', 'w') as f:
    for item in all_links_from_year.keys():
        f.write(item + "\n")
        for urle in all_links_from_year[item]:
            f.write(urle + "\n")
