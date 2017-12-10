from selenium import webdriver
from selenium.webdriver.support.ui import Select

path = 'https://prog.nfz.gov.pl/app-jgp/KatalogJGP.aspx'

driver = webdriver.Firefox()
driver.get(path)


def get_all_options(webdriver, contener):
    """Get all options from menu, return dictionary with value and text"""
    selected = Select(webdriver.find_element_by_name(contener))
    options = []
    options_text = []
    for option in selected.options:
        options.append(option.get_attribute('value'))
        options_text.append(option.text)

    return dict(zip(options[1:], options_text[1:]))


# get years
years_options = get_all_options(driver, 'ctl00$ContentPlaceHolder2$ddlSymylacjaJGP')

all_links_from_year = {}

for option in years_options.keys():
    # select years
    selected_year = Select(driver.find_element_by_name('ctl00$ContentPlaceHolder2$ddlSymylacjaJGP'))
    selected_year.select_by_value(option)
    # get diseases
    diseases_options = get_all_options(driver, 'ctl00$ContentPlaceHolder2$ddlKatalogJGP')
    # links from all years
    all_links_from_year[years_options[option]] = []
    # links from all diseases in year
    links_from_year = []

    # select disease
    for option2 in diseases_options.keys():
        selected_disease = Select(driver.find_element_by_name('ctl00$ContentPlaceHolder2$ddlKatalogJGP'))
        selected_disease.select_by_value(option2)
        # links in disease
        elinks = []
        elinks = driver.find_elements_by_xpath("//a[@href]")
        links = []
        for elink in elinks:
            links.append(elink.get_attribute('href'))
        links_from_year += links[3:]
    all_links_from_year[years_options[option]] = links_from_year

# write to file
with open('links.txt', 'w') as file:
    for year in all_links_from_year.keys():
        file.write(year + "\n")
        for urle in all_links_from_year[year]:
            file.write(urle + "\n")
