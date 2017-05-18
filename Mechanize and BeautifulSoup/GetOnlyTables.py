import sys
from urllib2 import urlopen, URLError
from argparse import ArgumentParser
from bs4 import BeautifulSoup


def parse_arguments():
    """ Process command line arguments """
    parser = ArgumentParser(description='Grabs tables from html')
    parser.add_argument('-u', '--url', help='url to grab from',
                        required=True)
    args = parser.parse_args()
    return args


def parse_rows(rows):
    """ Get data from rows """
    results = []
    for row in rows:
        table_headers = row.find_all('th')
        if table_headers:
            results.append([headers.get_text() for headers in table_headers])

        table_data = row.find_all('td')
        if table_data:
            results.append([data.get_text() for data in table_data])
    return results


def main():
    # Get arguments
    args = parse_arguments()
    if args.url:
        url = args.url

    # Make soup
    try:
        resp = urlopen(url)
    except URLError as e:
        print 'An error occured fetching %s \n %s' % (url, e.reason)   
        return 1
    soup = BeautifulSoup(resp.read(),'html.parser')

    # Get table
    try:
        table = soup.find('table')
    except AttributeError as e:
        print 'No tables found, exiting'
        return 1

    # Get rows
    try:
        rows = table.find_all('tr')
    except AttributeError as e:
        print 'No table rows found, exiting'
        return 1

    # Get data
    table_data = parse_rows(rows)

    # Print data
    f = open('netflixNew1.txt','w')
    for i in table_data:
       print '\t'.join(i)
       f.write('\t'.join(i) + '\n')
    f.close()


#if __name__ == '__main__':
#    status = main()
#    sys.exit(status)
main()
