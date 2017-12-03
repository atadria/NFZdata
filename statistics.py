from extractor import get_sum_of_all_cardiograms_from
from file_reader import retrieve_urls_for_year

years_sums = []
for i in range(2009, 2016):
    print(i)
    urls = retrieve_urls_for_year(i)
    particular_year_sum = 0
    for url in urls:
        particular_year_sum += get_sum_of_all_cardiograms_from(url)
        print(particular_year_sum)
    years_sums.append(particular_year_sum)
    print(years_sums, str(i))
