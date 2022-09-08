import argparse
import requests
import csv
import logging
import re
import io
import datetime
# other imports go here

#config for log file: Needs file name 
#LOG_FILENAME = ''
#logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)

def download_data(url):
    '''pulls down web log file as a string'''
    file = requests.get(url)
    return file.text

def csv_process(file):
    image_hits = 0
    browser_dict = {
        'IE': 0,
        'Safari': 0,
        'Chrome': 0,
        'Firefox': 0
    }
    csv_reader = csv.reader(io.StringIO(file))
    for i, row in enumerate(csv_reader):
        path_to_file = row[0]
        datetime_accessed = row[1] # parse this using dateime.datetime.strptim()
        try:
            datetime_accessed = datetime.datetime.strptime(row[1], '%Y/%m/%d %I:%M:%S')
        except ValueError:
            pass
        browser = row[2]
        status = row[3]
        request_size = row[4]
        print(row)

        if re.search("gif|jpe?g|png", path_to_file.lower()):
            image_hits += 1
        #check browser and update dict
        elif re.search("", browser):
            pass
    
    avg_hits = image_hits/(i + 1) * 100
    print(f'Image requests account for {avg_hits}% of all requests.')
   

def main(url):
    print(f"Running main with URL = {url}...")
    content = download_data(url)
    doc = csv_process(content)
    return doc

if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
    
