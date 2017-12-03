def retrieve_urls_for_year(year):
    urls = []
    read_line = False
    with open('links.txt', 'r') as inputFile:
        for line in inputFile.readlines():
            if line[4:8] == str(year):
                read_line = True
                continue
            if read_line and line[0:3] != 'Rok':
                urls.append(line)
            elif read_line and line[4:8] != str(year):
                return urls
        return urls
