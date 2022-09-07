import argparse
import requests
import csv
import logging
import re
# other imports go here

#config for log file: Needs file name 
#LOG_FILENAME = ''
#logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)

def download_data(url):
    '''pulls down web log file and stores it as csv'''
    file = requests.get(url)
    return file.text
   

def main(url):
    print(f"Running main with URL = {url}...")
    content = download_data(url)
    return content

if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
    
