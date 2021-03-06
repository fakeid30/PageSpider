#!/usr/bin/env python3

import os
import argparse
from utilities import url_utilities, database_utilities

website_input = int(input("How many websites you want to parse?:"))
for i in range(1, website_input + 1):
    if (website_input > 0) and (website_input != 0):
        print("Enter your number " + str(i) + " website:")
        website_input -= 1
    url_list_file = input()
    with open('input.txt', 'w') as f:
        f.write(url_list_file)


def main(database: str, url_list_file: str):
    big_word_list = []
    print("we are going work with " + database)
    print("we are going scan " + url_list_file)
    urls = url_utilities.load_urls_from_file(url_list_file)
    for url in urls:
        print("reading " + url)
        page_content = url_utilities.load_page(url=url)
        words = url_utilities.scrape_page(page_contents=page_content)
        big_word_list.extend(words)

    abs_file_path = os.path.abspath(__file__)
    os.chdir(os.path.dirname(abs_file_path))
    path = os.path.join(os.getcwd(), "words.db")
    database_utilities.create_database(database_path=path)
    database_utilities.save_words_to_database(database_path=path, words_list=big_word_list)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-db", "--database", help="SQLite File Name")
    parser.add_argument("-i", "--input", help="File containing urls to read")
    args = parser.parse_args()
    database_file = args.database
    input_file = args.input
    main(database=database_file, url_list_file=input_file)
