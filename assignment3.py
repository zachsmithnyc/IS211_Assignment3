import argparse
import requests
import csv
import re
import io
import datetime
# other imports go here

def download_data(url):
    '''pulls down web log file as a string'''
    file = requests.get(url)
    return file.text

def csv_process(file):
    image_hits = 0

    #dict to store browser hits
    browser_dict = {
        'IE': 0,
        'Safari': 0,
        'Chrome': 0,
        'Firefox': 0
    }
    #dict to store hourly hits
    hour_dict = {}
   
    csv_reader = csv.reader(io.StringIO(file))
    for i, row in enumerate(csv_reader):
        path_to_file = row[0]
        datetime_accessed = row[1] # parse this using dateime.datetime.strptim()
        browser = row[2]
        status = row[3]
        request_size = row[4]
        #print(row)

        if re.search(r"gif|jpe?g|png", path_to_file.lower()): #searches for image file extensions at the end of a string
            image_hits += 1
        #check browser and update dict
        if re.search(r"\bMSIE\b", browser.upper()):
            browser_dict['IE'] += 1
        elif re.search(r"\bfirefox\b", browser.lower()):
            browser_dict['Firefox'] += 1
        elif re.search(r'\bsafari\b', browser.lower()) and re.search(r'\bchrome\b', browser.lower()):
            browser_dict['Chrome'] += 1
        else:
            browser_dict["Safari"] += 1

    avg_hits = image_hits/(i + 1) * 100
    print(f'Image requests account for {avg_hits}% of all requests.')
    popular = max(browser_dict, key=browser_dict.get)
    print(f'The most popular browser is {popular} with {browser_dict["Chrome"]} hits.')
    
   

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
    
